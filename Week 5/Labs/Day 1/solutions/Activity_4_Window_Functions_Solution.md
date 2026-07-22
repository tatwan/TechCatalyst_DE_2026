# Activity 4 Solution: Window Functions

Instructor reference. Replace `<YOUR_NAME>` with the student's schema.

```sql
USE ROLE DE;
USE WAREHOUSE COMPUTE_WH;
USE DATABASE TECHCATALYST;
USE SCHEMA TECHCATALYST.<YOUR_NAME>;

-- W1: Rank trading days by close price, highest = 1.
SELECT
  trade_date,
  close_price,
  DENSE_RANK() OVER (ORDER BY close_price DESC) AS price_rank
FROM W5D1_STOCK
ORDER BY price_rank;

-- W2: Previous close and daily change.
SELECT
  trade_date,
  close_price,
  LAG(close_price) OVER (ORDER BY trade_date) AS prev_close,
  close_price - LAG(close_price) OVER (ORDER BY trade_date) AS daily_change
FROM W5D1_STOCK
ORDER BY trade_date;

-- W3: Running maximum and running average close.
SELECT
  trade_date,
  close_price,
  MAX(close_price) OVER (ORDER BY trade_date) AS running_max_close,
  ROUND(AVG(close_price) OVER (ORDER BY trade_date), 2) AS running_avg_close
FROM W5D1_STOCK
ORDER BY trade_date;

-- W4: 3-day moving average.
SELECT
  trade_date,
  close_price,
  ROUND(
    AVG(close_price) OVER (
      ORDER BY trade_date
      ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ),
    2
  ) AS moving_avg_3d
FROM W5D1_STOCK
ORDER BY trade_date;

-- W5: Biggest single-day gain (returns both 2024-07-08 and 2024-07-11, each +5).
WITH changes AS (
  SELECT
    trade_date,
    close_price - LAG(close_price) OVER (ORDER BY trade_date) AS daily_change
  FROM W5D1_STOCK
)
SELECT trade_date, daily_change
FROM changes
WHERE daily_change = (SELECT MAX(daily_change) FROM changes)
ORDER BY trade_date;

-- W6: Combine all window functions into a single query.
SELECT
  trade_date,
  close_price,
  LAG(close_price) OVER (ORDER BY trade_date) AS prev_close,
  close_price - LAG(close_price) OVER (ORDER BY trade_date) AS daily_change,
  ROUND(
    AVG(close_price) OVER (
      ORDER BY trade_date
      ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ),
    2
  ) AS moving_avg_3d,
  MAX(close_price) OVER (ORDER BY trade_date) AS running_max_close,
  ROUND(AVG(close_price) OVER (ORDER BY trade_date), 2) AS running_avg_close,
  DENSE_RANK() OVER (ORDER BY close_price DESC) AS price_rank
FROM W5D1_STOCK
ORDER BY trade_date;

-- ===== Part B: TPC-H stretch =====
USE SCHEMA SNOWFLAKE_SAMPLE_DATA.TPCH_SF1;

-- S1: grand total of sales on every yearly row.
SELECT
  YEAR(o_orderdate) AS order_year,
  COUNT(*) AS num_orders,
  SUM(o_totalprice) AS tot_sales,
  SUM(SUM(o_totalprice)) OVER () AS grand_total
FROM orders
GROUP BY order_year
ORDER BY order_year;

-- S2: top 3 months by total sales within each year (rank DESC for top, not bottom).
WITH monthly AS (
  SELECT
    YEAR(o_orderdate) AS order_year,
    MONTH(o_orderdate) AS order_month,
    COUNT(*) AS num_orders,
    SUM(o_totalprice) AS tot_sales
  FROM orders
  GROUP BY order_year, order_month
),
ranked AS (
  SELECT
    order_year,
    order_month,
    num_orders,
    tot_sales,
    RANK() OVER (PARTITION BY order_year ORDER BY tot_sales DESC) AS month_rank
  FROM monthly
)
SELECT *
FROM ranked
WHERE month_rank <= 3
ORDER BY order_year, month_rank;
```

Note on S2: the 2025 reference solution ranked `ORDER BY tot_sales` (ascending), which returns the bottom three months. Top three needs `DESC`.
