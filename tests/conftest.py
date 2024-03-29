import pytest
from app import create_app, db


@pytest.fixture(autouse=True)
def set_test_env_vars(monkeypatch):
    monkeypatch.setenv('TEST_SECRET_KEY', 'test')
    monkeypatch.setenv("DEBUGGING_VERBOSITY", "4")
    # connection to SQLExpress
    connection_string = r'DRIVER={ODBC Driver 13 for SQL Server};' + "SERVER={0};DATABASE={1};UID={2};PWD={3}".format('.\SQLEXPRESS', 'labelmanagertestdb', 'testuser', 'Volunteer2019')
    monkeypatch.setenv('SQLALCHEMY_DATABASE_URI', connection_string) 


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    print('creating app with test vars')

    app = create_app('test')
    app.testing = True

    ctx = app.app_context()
    ctx.push()
    yield app

    ctx.pop()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


@pytest.fixture
def db_client():
    app = create_app('test')
    app.testing = True
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    db.create_all()

    yield client

    db.session.remove()
    db.drop_all()
    ctx.pop()


@pytest.fixture
def db_runner():
    app = create_app('test')
    app.testing = True
    runner = app.test_cli_runner()
    ctx = app.app_context()
    ctx.push()
    db.create_all()

    yield runner

    db.session.remove()
    db.drop_all()
    ctx.pop()


@pytest.fixture
def database():
    return db


def pytest_configure(config):
    """ A test marker named "smoke" is used to run only a subset of tests
    Feel free to create your own markers. Add them to your tests with
    a "@pytest.mark.mymarker" and run only those tests with
    'pytest -m 'mymarker'
    """
    config.addinivalue_line(
        "markers", "smoke"
    )