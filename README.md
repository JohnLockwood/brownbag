
# A FastAPI REST API on EKS / (Or Lamda?)

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/JohnLockwood/brownbag)


Assumptions:  
* Python 3.6 plus.
* AWS cli installed and configured with broad rights and default region set.

## Todo for brownbag:

- [x] Decide on Pycharm or All Products by 10/25/2020.  All products is $149 / year.  Is this a no-brainer?
- [x] Preliminary code based on FastAPI samples [here](https://fastapi.tiangolo.com/tutorial/sql-databases/) or better yet [see code for that](https://github.com/tiangolo/fastapi/tree/master/docs_src/sql_databases).
- [ ] Secrets.  Should be only one environment variable, "environment" (= "development", "staging", "production", etc.).  The rest is read out of SSM Key Store. We can do this without Helm with a [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/).  (Search sample for game-demo.)
- [ ] Cloudformation stack 
- [ ] buildspec.yml and appspec.yml
- [ ] Be aware of pricing as you go along. [KMS](https://aws.amazon.com/kms/pricing/) (used by System Manager Param Store) appears to be OK if using AWS managed CMKs.  If you make your own it's $1.00 per month.


## Future / Out of Scope for Brownbag / Optional
- [ ] Alembic migrations
- [ ] [Async SQL](https://github.com/tiangolo/fastapi/tree/master/docs_src/async_sql_databases) and associated article in FastAPI docs - Optional

## Security Notes:

* secrets directory is git ignored and has never leaked to git.  Fine for now, but for multiple developers consider moving out of repo altogether.
* Although PostgreSQL password is not in the docker-compose.yml or vcs, the way it's done would leak it to the PostgreSQL container locally.  Since this image is intended to be local only and will never be pushed anywhere, this is not a concern for now.  