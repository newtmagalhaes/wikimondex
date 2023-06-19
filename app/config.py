from os import getenv


class BaseConfig:
    ENV = None
    DEBUG = False

    # Flask-Restx
    RESTX_MASK_SWAGGER = False

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class Development(BaseConfig):
    ENV = 'Development'
    DEBUG = True

CONFIG = {
    'dev': Development,
}

app_config = CONFIG[getenv('ENV', 'dev')]
