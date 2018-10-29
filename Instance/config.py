#default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my_key'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True

app_config{
   'development':DevelopmentConfig
   'production':ProductionConfig
   'testing':TestingConfig
}