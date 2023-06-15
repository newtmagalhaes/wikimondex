from ..db import db
from ..models import Especie
from ..utils.iniciais import ESPECIES


def reset_db():
    db.drop_all()
    db.create_all()

    db.session.add_all(
        [Especie(**pokemon) for pokemon in ESPECIES]
    )
    db.session.commit()
