from ..db import db
from ..utils.tipos import Poketipo
from sqlalchemy import CheckConstraint



class Especie(db.Model):
    __tablename__ = 'especies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    primary_type = db.Column(db.Enum(Poketipo), nullable=False, default=Poketipo.NORMAL)
    secondary_type = db.Column(db.Enum(Poketipo))

    origin_id = db.Column(db.Integer, db.ForeignKey('especies.id'))

    origin = db.relationship("Especie", remote_side=[id], backref='evolutions')
    __table_args__ = (
        CheckConstraint('primary_type != secondary_type', name='check_primary_secondary_type'),
        CheckConstraint('(primary_type != {normal_type} AND secondary_type IS NOT NULL) OR (primary_type = {normal_type} AND secondary_type IS NULL)'.format(normal_type=Poketipo.NORMAL), name='check_secondary_type_with_primary_type')
    )
    especimes = db.relationship("Especime", back_populates='especie')
