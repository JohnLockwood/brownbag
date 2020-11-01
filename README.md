
# A FastAPI REST API on EKS / (Or Lamda?)

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/JohnLockwood/brownbag)

Assumptions:  
* Python 3.6 plus.
* AWS cli installed and configured with broad rights and default region set.

## Todo for brownbag:

- [x] Decide on Pycharm or All Products by 10/25/2020.  All products is $149 / year.  Is this a no-brainer?
- [x] Preliminary code based on FastAPI samples [here](https://fastapi.tiangolo.com/tutorial/sql-databases/) or better yet [see code for that](https://github.com/tiangolo/fastapi/tree/master/docs_src/sql_databases).
- [ ] Secrets. This is in progress, especially with CFN pusher.  [ ] NOTE: The way I was doing it -- segmenting by app and ID -- is **explicitly NOT** the [12-Factor Recommendation](https://12factor.net/config).  Preliminary idea is that what's needed to make that work is:
    * For EKS, have CFN populate N Secrets from AWS SSM Parameter Store Secure Strings.  See [How do you build 12 Factor Apps Using Kubernetes](https://www.mirantis.com/blog/how-do-you-build-12-factor-apps-using-kubernetes/) for how to wire up Secrets into environment, but basic code looks like:
        ```
        env:
            - name: SECRET_USERNAME
            valueFrom:
                secretKeyRef:
                name: mysecret
                key: username
            - name: SECRET_PASSWORD
            valueFrom:
                secretKeyRef:
                name: mysecret
                key: password
            - ETC...
        ```
        Note that even though the keys the app reads should no longer be scoped to "dev", "production", etc but rather be bare keys, the buildspec or other code reading them may do this trick in reading them out of SSM.  GOOD ENOUGH FOR NOW.
    * See the AWS article on [Defense in Depth](https://aws.amazon.com/blogs/containers/using-eks-encryption-provider-support-for-defense-in-depth/). This is both more secure and harder to do.
- [ ] Cloudformation stack 
- [ ] buildspec.yml and appspec.yml
- [ ] Be aware of pricing as you go along. [KMS](https://aws.amazon.com/kms/pricing/) (used by System Manager Param Store) appears to be OK if using AWS managed CMKs.  If you make your own it's $1.00 per month.

## Future / Out of Scope for Brownbag / Optional
- [ ] Alembic migrations
- [ ] [Async SQL](https://github.com/tiangolo/fastapi/tree/master/docs_src/async_sql_databases) and associated article in FastAPI docs - Optional

## Security Notes:

* secrets directory is git ignored and has never leaked to git.  Fine for now, but for multiple developers consider moving out of repo altogether.
* Although PostgreSQL password is not in the docker-compose.yml or vcs, the way it's done would leak it to the PostgreSQL container locally.  Since this image is intended to be local only and will never be pushed anywhere, this is not a concern for now.  