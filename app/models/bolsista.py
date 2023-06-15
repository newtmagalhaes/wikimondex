from ..db import db
from datetime import datetime

class Bolsista(db.Model):
    __tablename__ = 'bolsistas'

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, nullable = False)
    _data_nascimento = db.Column('data_nascimento', db.Date, nullable=False)
    foto_perfil_key = db.Column(db.String, nullable=True)

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        self._data_nascimento = datetime.strptime(value, '%Y-%m-%d').date()
