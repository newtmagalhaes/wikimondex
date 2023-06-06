from app import db

from ..utils.tipos import Poketipo


class Especie(db.Model):
    __tablename__ = 'especies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    primary_type = db.column(db.Enum(Poketipo), nullable=False, default=Poketipo.NORMAL)
    secondary_type = db.column(db.Enum(Poketipo))

    origin_id = db.Column(db.ForeignKey('especies.id'))

    origin = db.relationship("Especie", back_populates='origin')