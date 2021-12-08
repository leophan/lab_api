from os import environ

from flask import Flask

from api import routes
from api.models.sqla import db
from config import config


def create_app(env):
    flask_app = Flask(__name__)

    flask_app.config.from_object(config.get(env))

    db.init_app(flask_app)
    db.create_all(app=flask_app)

    routes.init_app(flask_app)

    return flask_app


app = create_app(environ.get('env') or 'local')
