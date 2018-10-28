#default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my_key'

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

class TestingConfig(BaseConfig):
    TESTING = True

class StagingConfig(BaseConfig):
    DEBUG = True

