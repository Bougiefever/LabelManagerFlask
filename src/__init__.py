from flask import Flask, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config_list
import urllib

bootstrap = Bootstrap()
db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name):
    app = Flask(__name__)
    settings = config_list[config_name]
    app.config.from_object(settings)
    settings.init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    ma.init_app(app)

    from . import main, api
    app.register_blueprint(main.bp)
    app.register_blueprint(api.bp)

    return app
