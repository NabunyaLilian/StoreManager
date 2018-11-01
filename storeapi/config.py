import os
basedir = os.path.abspath(os.path.dirname(__file__))
#default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my_key'
    DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DATABASE_URI = "postgresql://localhost/storedb"
    ENV = 'development'

class ProductionConfig(BaseConfig):
    DEBUG = False

class TestingConfig(BaseConfig):
    TESTING = True
    DATABASE_URI = "postgresql://localhost/testdb"
    ENV = 'development'
class StagingConfig(BaseConfig):
    DEBUG = True

app_configuration = {
    "development" : DevelopmentConfig,
    "testing" : TestingConfig
}    