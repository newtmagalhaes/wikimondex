from ..db import db
from datetime import datetime
from sqlalchemy.event import listens_for
from datetime import date

class Bolsista(db.Model):
    __table_name__ = 'bolsista'

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, nullable = False)
    _data_nascimento = db.Column('data_nascimento', db.Date, nullable=False)
    foto_perfil_filekey = db.Column(db.String, nullable=True)

    __table_args__ = (
        db.CheckConstraint('data_nascimento <= CURRENT_DATE', name='check_data_nascimento'),
        db.CheckConstraint('LENGTH(cpf) = 11', name='check_cpf'),
    )

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        self._data_nascimento = datetime.strptime(value, '%Y-%m-%d').date()


def name_to_upper(mapper, connection, target):
    target.nome = target.nome.upper()

listens_for(Bolsista, 'before_insert')(name_to_upper)