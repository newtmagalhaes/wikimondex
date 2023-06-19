from ..db import db
from ..utils.tipos import Poketipo


class Especie(db.Model):
    __tablename__ = 'especies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    primary_type = db.Column(db.Enum(Poketipo), nullable=False, default=Poketipo.NORMAL)
    secondary_type = db.Column(db.Enum(Poketipo))

    origin_id = db.Column(db.Integer, db.ForeignKey('especies.id'))

    origin = db.relationship("Especie", remote_side=[id], backref='evolutions')
    especimes = db.relationship("Especime", back_populates='especie')
