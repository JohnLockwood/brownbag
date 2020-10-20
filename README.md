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
|Local build and run|04:00:00|2:20:00|Secrets, docker-compose, etc.  In flight.  By about 2:20, docker-compose running postgres, can connect|

## Future / Out of Scope for Brownbag / Optional
- [ ] Alembic migrations
- [ ] [Async SQL](https://github.com/tiangolo/fastapi/tree/master/docs_src/async_sql_databases) and associated article in FastAPI docs - Optional

## Security Notes:

* secrets directory is git ignored and has never leaked to git.  Fine for now, but for multiple developers consider moving out of repo altogether.
* Although PostgreSQL password is not in the docker-compose.yml or vcs, the way it's done would leak it to the PostgreSQL container locally.  Since this image is intended to be local only and will never be pushed anywhere, this is not a concern for now.  