from flask import Flask

from .config import app_config


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config)

    return app
