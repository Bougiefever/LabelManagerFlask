import pytest


@pytest.mark.smoke
def test_index(client):
    """ Simple smoke test to determine that the site can load """
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello there"


@pytest.mark.smoke
def test_config(app):
    """ Test that the config settings were loaded  """
    assert app.config.get('SECRET_KEY') == 'test'

