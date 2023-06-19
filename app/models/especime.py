from datetime import datetime,date
from sqlalchemy import event


from ..db import db

class Especime(db.Model):
    __table_name__ = 'especime'

    id = db.Column(db.Integer,primary_key=True)
    apelido = db.Column(db.String, nullable=False)
    altura = db.Column(db.Float, nullable = False)
    peso = db.Column(db.Float, nullable = False)
    data_cadastro = db.Column('data_cadastro', db.Date, nullable=False)

    id_bolsista = db.Column(db.Integer, db.ForeignKey('bolsistas.id'), nullable=False)
    id_especie = db.Column(db.Integer, db.ForeignKey('especies.id'), nullable=False)
    id_foto_especime = db.Column(db.String, nullable=False, default = "")

    especie = db.relationship('Especie', back_populates='especimes', uselist=False)

@event.listens_for(Especime, 'before_insert')
def set_data_cadastro(mapper, connection, target):
    target.data_cadastro = date.today()
