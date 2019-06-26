import os

import sys
import click
from flask_migrate import Migrate, upgrade
from src import create_app, db
from src.models.image import Image
from src.models.job import Job
import config
from config import config_list
from flask.cli import with_appcontext

click.disable_unicode_literals_warning = True


config_name = os.getenv('FLASK_CONFIG') or 'default'
application = create_app(os.getenv('FLASK_CONFIG') or 'default')
print(config_name)
print(application.config['SQLALCHEMY_DATABASE_URI'])


# ensure the instance folder exists
# try:
#     os.makedirs(application.instance_path)
# except OSError:
#     pass

migrate = Migrate(application, db)


@application.route('/info')
def info():
    environ = os.getenv('FLASK_CONFIG')
    server = os.getenv('SQL_SERVER_NAME')
    conn = config.ProductionConfig().connection_string
    info = 'config type = ' + environ \
        + '<br />sql_server_name = ' + server \
        + '<br />connection = ' + conn
    return info


@application.route('/testdb')
def test_db():
    eng = db.get_engine()
    connect = eng.connect()
    data = connect.execute("SELECT @@version;")
    return type(data)


@application.shell_context_processor
def make_shell_context():
    return dict(db=db, Job=Job, Image=Image)


@application.cli.command()
@with_appcontext
def resetdatabase():
    st = "using config settings: {}".format(os.getenv('FLASK_CONFIG') or 'default')
    click.echo(st)
    db.drop_all()
    db.create_all()
    click.echo("database was reset")

@application.cli.command()
def showenv():
    env = os.getenv('FLASK_CONFIG')
    print(env)