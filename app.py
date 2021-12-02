from flask import Flask
from api.models.db import DB

MAX_CONTENT_LENGTH = 2 * 1024 * 1024
# MAX_CONTENT_LENGTH = 2 * 1024
DB_URL = 'sqlite:///lab_sqlite.db'
# DB_URL = 'sqlite://'

# TODO: refactor to be abc to connect database
db = DB(DB_URL)
engine = db.connect()

def create_app():
    # TODO: load config from file `instance_relative_config=True`
    flask_app = Flask(__name__, instance_relative_config=True)
    # TODO: refactor to handle msg large file
    flask_app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

    from api import routes
    routes.init_app(flask_app)

    return flask_app


app = create_app()
