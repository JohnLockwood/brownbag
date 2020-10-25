from pytest import fixture
from app.core.config import Config


@fixture
def config():
    return Config()


def test_can_create_config(config):
    assert config is not None
    assert Config.APP_NAME == 'api'
    assert config.app == 'api'
    assert config.environment == 'development'


def test_get_value_returns_value_if_key_is_good(config):
    value = config.get_value('db/name')
    assert value is not None
    assert value == 'postgres'


def test_get_value_returns_value_if_key_starts_with_slash(config):
    value = config.get_value('/db/name')
    assert value is not None
    assert value == 'postgres'


def test_get_value_returns_none_if_key_invalid(config):
    # Key invalid because of bad key
    value = config.get_value('bogus/key/is/bogus')
    assert value is None

    # Key is good, but mess up the object
    config.environment = "bogus/environment"
    value = config.get_value('db/name')
    assert value is None


def test_get_connection_string(config):
    value = config.get_connection_string()
    assert "None" not in value
    assert "localhost" not in value


def test_get_connection_string_overriding_host(config):
    value = config.get_connection_string(host='localhost')
    assert "None" not in value
    assert "localhost" in value
