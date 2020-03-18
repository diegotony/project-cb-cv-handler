import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    # DB_URL = os.getenv('DB_URL', '')
    DB_USER = os.getenv('DB_USER', 'user')
    DB_PASS = os.getenv('DB_PASS', 'password')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'flask_boilerplate_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# class TestingConfig(Config):
#     DEBUG = True
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
#         os.path.join(basedir, 'flask_boilerplate_test.db')
#     PRESERVE_CONTEXT_ON_EXCEPTION = False
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    # "mysql://user:password@mysql/db"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_TRACK_MODIFICATIONS = True

config_by_name = dict(
    dev=DevelopmentConfig,
    # test=TestingConfig,
    prod=ProductionConfig
)
