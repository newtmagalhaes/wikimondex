import pytest
from app import create_app
from app.db import db


@pytest.fixture(scope="session")
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    with app.app_context():
        yield app.test_client()


def create_entities(*entities):
    db.session.add_all(entities)
    db.session.commit()


@pytest.fixture()
def setup_database(client):
    db.drop_all()
    db.create_all()
    yield create_entities
    db.drop_all()
