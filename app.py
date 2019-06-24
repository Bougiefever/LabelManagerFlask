import os
from dotenv import load_dotenv
import sys
import click
from flask_migrate import Migrate, upgrade
from src import create_app, db
from src.models.image import Image
from src.models.job import Job
import config
from config import config_list
from flask.cli import with_appcontext

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

#print(os.getenv('FLASK_CONFIG'))
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# ensure the instance folder exists
# try:
#     os.makedirs(app.instance_path)
# except OSError:
#     pass

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Job=Job, Image=Image)


@app.cli.command()
@with_appcontext
def resetdatabase():
    st = "using config settings: {}".format(os.getenv('FLASK_CONFIG') or 'default')
    click.echo(st)
    db.drop_all()
    db.create_all()
    click.echo("database was reset")