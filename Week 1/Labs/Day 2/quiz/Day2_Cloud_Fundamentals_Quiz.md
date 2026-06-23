# Day 2: Cloud Fundamentals — Don't Burn the Budget
# Score 100

## Q1: You run a query in BigQuery. Google handles the servers, scaling, and patching; you just bring the SQL and the data. Which service model is that closest to?
- [ ] IaaS — you manage the OS and the machine
- [x] PaaS / managed service — you bring code and data
- [ ] SaaS — a finished app you just log into
- [ ] On-prem — your own server in a closet
::time=20

## Q2: Your nightly claims CSV lands in Google Cloud Storage. Your friend on the AWS team would drop the same file into…?
- [ ] Amazon Redshift
- [ ] Amazon EC2
- [ ] Amazon SageMaker
- [x] Amazon S3
::time=15

## Q3: In Activity 1 you watched BigQuery report "bytes processed." On on-demand pricing, what does the bill actually charge you for?
- [x] The amount of data the query scans
- [ ] The number of rows it returns
- [ ] How long you stared at the results
- [ ] How many columns the table has
::time=20

## Q4: Someone spins up a VM for a 5-minute nightly job, then forgets it and it runs 24/7. Which pricing meter just wrecked the budget?
- [ ] Storage size (GB-month)
- [x] Time — compute left running
- [ ] Requests / API calls
- [ ] Network egress
::time=15

## Q5: A new analyst only needs to read one BigQuery dataset. What's the right IAM move?
- [ ] Give them Project Owner — it is faster for everyone
- [ ] Share your own login so they can sign in as you
- [ ] Make the dataset public so anyone can read it
- [x] Grant the least-privilege role: read-only on that dataset
::time=20

## Q6: The telematics pilot needs a risk score within seconds of each driving event. Batch or streaming?
- [x] Streaming — score each event as it arrives
- [ ] Batch — run it nightly and hope nobody minds the delay
- [ ] Neither — email everyone a spreadsheet
- [ ] Print it out and mail it
::time=15

## Q7: Why set cloud budget alerts at 50% and 90% instead of only at 100%?
- [ ] Because 100%-only alerts are against cloud law
- [ ] So the monthly bill looks more impressive
- [x] So you can act before you overspend, not after
- [ ] Because alerts get more expensive at 100%
::time=20
