# A FastAPI REST API on EKS / (Or Lamda?)

Assumptions:  
* Python 3.6 plus.
* AWS cli installed and configured with broad rights and default region set.


## Todo for brownbag:

- [ ] Decide on Pycharm or All Products by 10/25/2020.  All products is $149 / year.  Is this a no-brainer?
- [ ] Preliminary code based on FastAPI samples [here](https://fastapi.tiangolo.com/tutorial/sql-databases/) or better yet [see code for that](https://github.com/tiangolo/fastapi/tree/master/docs_src/sql_databases).  
- [ ] Secrets.  Should be only one environment variable, "environment" (= "development", "staging", "production", etc.).  The rest is read out of SSM Key Store. We can do this without Helm with a [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/).  (Search sample for game-demo.)
- [ ] Cloudformation stack 
- [ ] buildspec.yml and appspec.yml
- [ ] Be aware of pricing as you go along. [KMS](https://aws.amazon.com/kms/pricing/) (used by System Manager Param Store) appears to be OK if using AWS managed CMKs.  If you make your own it's $1.00 per month.


|Task|Estimated (hrs)|Actual|Notes|
|:---|--------------:|-----:|:----|
|Preliminary API Code|05:00:00|00:06:37|So far just barely reworked and committed code.  Done when running in pycharm and venv I suppose also needs rework based on Secrets work.|


## Future / Out of scope for Brownbag / Optional
- [ ] Alembic migrations
- [ ] [Async SQL](https://github.com/tiangolo/fastapi/tree/master/docs_src/async_sql_databases) and associated article in FastAPI docs - Optional