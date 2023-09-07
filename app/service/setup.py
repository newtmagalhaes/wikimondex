from ..db import db
from ..models import Especie,Especime,Bolsista
from ..utils.iniciais import ESPECIES,BOLSISTAS,ESPECIMES


def reset_db():
    db.drop_all()
    db.create_all()

    db.session.add_all(
        [Especie(**pokemon) for pokemon in ESPECIES],
    )
    db.session.add_all(
        [Bolsista(**pokemon) for pokemon in BOLSISTAS]
    )
    db.session.add_all(
        [Especime(**pokemon) for pokemon in ESPECIMES],
    )
    db.session.commit()
