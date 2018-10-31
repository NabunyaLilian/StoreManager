import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'suprise!'


class ProductionConfig(BaseConfig):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DEV_DB = 'testdb'

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    TEST_DATABASE = 'storedb'

