from ..db import db
from ..models import Especie


def commit(*instances):
    if instances:
        db.session.add_all(instances)
    db.session.commit()


def create_especie(data: dict) -> Especie:
    nova_especie = Especie(**data)

    commit(nova_especie)
    return nova_especie
