from os import getenv


class BaseConfig:
    ENV = None
    DEBUG = False


class Development(BaseConfig):
    ENV = 'Development'
    DEBUG = True

CONFIG = {
    'dev': Development,
}

app_config = CONFIG[getenv('ENV', 'dev')]
