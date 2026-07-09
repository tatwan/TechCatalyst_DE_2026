"""Week 3 Day 3 mini-project solution: medallion ETL (S3 raw -> GCS bronze -> GCS silver).

Flow:
  1. EXTRACT  read raw bytes from a PUBLIC S3 bucket (anonymous, via boto3), or
              from the local fallback file with --local.
  2. BRONZE   land the raw bytes unchanged in your GCS bucket (or local dir),
              partitioned by ingest_date. Bronze is immutable: never edit it.
  3. SILVER   clean with pandas into a typed table, write parquet, upload to GCS
              (or local dir). An optional Polars version shows the same work.

Auth: Application Default Credentials. Run once: `gcloud auth application-default login`.
No key files. Uploads use the google-cloud-storage client.

Run from your project folder (the folder that contains data/):
    uv run python medallion_etl_solution.py            # S3 -> GCS
    uv run python medallion_etl_solution.py --local    # fully local, no cloud
    uv run python medallion_etl_solution.py --local --polars  # optional stretch
"""
import argparse
import io
from datetime import date
from pathlib import Path

import pandas as pd

# ---- Config: edit for your setup ----
SOURCE_BUCKET = "techcatalyst-de-2026"        # public S3 source (read-only)
SOURCE_KEY = "raw/weather/weather_raw.csv"
GCP_PROJECT = "your-gcp-project-id"                  # your assigned project
GCS_BUCKET = "techcatalyst-de-2026-your-username-raw"
DATASET = "weather"
INGEST_DATE = date.today().isoformat()

LOCAL_RAW = Path("data/raw/weather_raw.csv")
LOCAL_BRONZE = Path("data/bronze")
LOCAL_SILVER = Path("data/silver")


def require_cloud_config() -> None:
    """Fail early if the editable cloud settings still contain placeholders."""
    if GCP_PROJECT == "your-gcp-project-id":
        raise ValueError("Set GCP_PROJECT to your assigned Google Cloud project ID.")
    if "your-username" in GCS_BUCKET:
        raise ValueError("Set GCS_BUCKET to your bucket name.")


def bronze_blob_path() -> str:
    """Return the GCS object name for the immutable bronze raw file."""
    return f"bronze/{DATASET}/ingest_date={INGEST_DATE}/{DATASET}_raw.csv"


def silver_blob_path() -> str:
    """Return the GCS object name for the cleaned silver parquet file."""
    return f"silver/{DATASET}/{DATASET}_clean.parquet"


# ---- 1. EXTRACT ----
def read_raw_from_s3() -> bytes:
    """Read the raw object from a public S3 bucket, anonymously (no AWS keys)."""
    import boto3
    from botocore import UNSIGNED
    from botocore.config import Config

    s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))
    obj = s3.get_object(Bucket=SOURCE_BUCKET, Key=SOURCE_KEY)
    return obj["Body"].read()


def read_raw_local() -> bytes:
    return LOCAL_RAW.read_bytes()


# ---- 2. BRONZE (land raw, unchanged) ----
def write_bronze_gcs(raw_bytes: bytes) -> str:
    """Upload raw bytes unchanged to the GCS bronze path and return the gs:// URI."""
    from google.cloud import storage

    require_cloud_config()
    blob_path = bronze_blob_path()
    client = storage.Client(project=GCP_PROJECT)
    blob = client.bucket(GCS_BUCKET).blob(blob_path)
    blob.upload_from_string(raw_bytes, content_type="text/csv")
    return f"gs://{GCS_BUCKET}/{blob_path}"


def write_bronze_local(raw_bytes: bytes) -> str:
    out_dir = LOCAL_BRONZE / DATASET / f"ingest_date={INGEST_DATE}"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{DATASET}_raw.csv"
    path.write_bytes(raw_bytes)
    return str(path)


# ---- 3. SILVER (clean with pandas) ----
def to_silver(raw_bytes: bytes) -> pd.DataFrame:
    df = pd.read_csv(io.BytesIO(raw_bytes))

    # normalize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # types: station is text, date is a date, the rest are numeric
    df["station"] = df["station"].astype(str).str.strip().str.upper()
    df["date"] = pd.to_datetime(df["date"].astype(str).str.strip(), errors="coerce")
    for col in ("tmax", "tmin", "prcp"):
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # row policy
    df = df.dropna(subset=["date"])                      # must have a date
    df = df.drop_duplicates(subset=["station", "date"])  # one row per station/day
    df["prcp"] = df["prcp"].fillna(0.0).clip(lower=0)    # missing precip = 0; no negatives
    df = df.dropna(subset=["tmax", "tmin"])              # need both temperatures

    # derived columns
    df["temp_range"] = df["tmax"] - df["tmin"]
    df["is_rainy"] = df["prcp"] > 0
    return df.reset_index(drop=True)


def write_silver_gcs(df: pd.DataFrame) -> str:
    """Write silver parquet locally, upload it to GCS, and return the gs:// URI."""
    from google.cloud import storage

    require_cloud_config()
    local_parquet = LOCAL_SILVER / DATASET / f"{DATASET}_clean.parquet"
    local_parquet.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(local_parquet, index=False)            # write locally first

    blob_path = silver_blob_path()
    client = storage.Client(project=GCP_PROJECT)
    blob = client.bucket(GCS_BUCKET).blob(blob_path)
    blob.upload_from_filename(local_parquet)             # then upload with ADC
    return f"gs://{GCS_BUCKET}/{blob_path}"


def write_silver_local(df: pd.DataFrame) -> str:
    out = LOCAL_SILVER / DATASET / f"{DATASET}_clean.parquet"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    return str(out)


# ---- Silver in Polars (the SAME clean, a different engine) ----
def to_silver_polars(raw_bytes: bytes):
    """The same silver transform as to_silver(), written in Polars.

    Note the API differences: Polars uses expressions inside with_columns and is
    multi-threaded by default. The result should match the pandas version row for
    row. (Polars is a different API from pandas, not a drop-in replacement.)
    """
    import polars as pl

    df = pl.read_csv(io.BytesIO(raw_bytes))
    df = df.rename({c: c.strip().lower() for c in df.columns})
    df = df.with_columns(
        pl.col("station").cast(pl.Utf8).str.strip_chars().str.to_uppercase(),
        pl.col("date").str.strptime(pl.Date, "%Y-%m-%d", strict=False),
        pl.col("tmax").cast(pl.Float64, strict=False),
        pl.col("tmin").cast(pl.Float64, strict=False),
        pl.col("prcp").cast(pl.Float64, strict=False),
    )
    df = df.drop_nulls(subset=["date"]).unique(subset=["station", "date"], keep="first")
    # missing precip -> 0, and no negatives (when/otherwise is version-stable)
    df = df.with_columns(
        pl.when(pl.col("prcp").is_null() | (pl.col("prcp") < 0))
          .then(0.0)
          .otherwise(pl.col("prcp"))
          .alias("prcp")
    )
    df = df.drop_nulls(subset=["tmax", "tmin"])
    df = df.with_columns(
        (pl.col("tmax") - pl.col("tmin")).alias("temp_range"),
        (pl.col("prcp") > 0).alias("is_rainy"),
    )
    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", action="store_true", help="run fully local, no cloud")
    parser.add_argument("--polars", action="store_true", help="run optional Polars stretch")
    args = parser.parse_args()

    # 1. EXTRACT
    raw_bytes = read_raw_local() if args.local else read_raw_from_s3()
    print(f"extracted {len(raw_bytes)} bytes of raw data")

    # 2. BRONZE
    bronze_uri = write_bronze_local(raw_bytes) if args.local else write_bronze_gcs(raw_bytes)
    print("bronze:", bronze_uri)

    # 3. SILVER
    df = to_silver(raw_bytes)
    print(f"silver rows: {len(df)}")
    print(df.groupby("station").size().to_dict())
    silver_uri = write_silver_local(df) if args.local else write_silver_gcs(df)
    print("silver:", silver_uri)

    if args.polars:
        pl_df = to_silver_polars(raw_bytes)
        print(f"polars silver rows: {pl_df.height} (should match the pandas count above)")
    else:
        print("polars stretch skipped")


if __name__ == "__main__":
    main()
