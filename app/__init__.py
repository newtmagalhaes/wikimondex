from flask import Flask

from .controller import blueprint
from .config import app_config
from .db import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config)
    app.register_blueprint(blueprint)

    init_db(app)

    return app

