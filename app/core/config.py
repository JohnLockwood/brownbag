import boto3
from botocore.exceptions import ClientError
import os

class Config:

    # Hard-coded centrally here.
    APP_NAME = 'api'

    # Must be set or all bets are off. This plus APP_NAME enables us to get everything we need from
    # SSM key-store
    KEY_ENVIRONMENT='RUN_ENVIRONMENT'

    KEY_HOST = 'db/host'
    KEY_USER = 'db/user'
    KEY_PASSWORD = 'db/password'
    KEY_DATABASE = 'db/name'

    """Read application configuration from SSM Parameter Key Store"""
    def __init__(self):
        self.environment = os.getenv(Config.KEY_ENVIRONMENT, default=None)
        if self.environment is None:
            raise Exception(f"Configuration error: environment must be set to etc. using key {Config.KEY_ENVIRONMENT}")
        self.app = Config.APP_NAME
        self.client = boto3.client('ssm')

    def get_value(self, key: str) -> str:
        """Return a value for a given key, adding the application and environment to the beginning of the key"""
        if key.startswith('/'):
            key = key[1:]
        try:
            full_key = f'/{self.app}/{self.environment}/{key}'
            response = self.client.get_parameter(Name=full_key, WithDecryption=True)
        except ClientError:
            return None
        return response["Parameter"]["Value"]

    def get_connection_string(self, host=None) -> str:
        """Returns a postgresql connection string for the environment.  Allow overriding host to be able to test
        from virtualenv, which requires localhost to connect to docker-compose postgres"""
        if not host:
            host = self.get_value(Config.KEY_HOST)
        user = self.get_value(Config.KEY_USER)
        password = self.get_value(Config.KEY_PASSWORD)
        database = self.get_value(Config.KEY_DATABASE)
        # return f'dbname={database} password={password} user={user} host={host} port=5432'
        return f"postgresql://{user}:{password}@{host}/{database}"
