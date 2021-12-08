class LocalConfig(object):
    debug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///local_sqlite.db"
    # MAX_CONTENT_LENGTH = 2 * 1024
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHMEY_ECHO = True

class DevConfig(object):
    debug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev_sqlite.db"
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(object):
    debug = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///prod_sqlite.db"
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'local': LocalConfig,
}