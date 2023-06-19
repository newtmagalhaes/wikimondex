from ..db import db
from datetime import datetime
from sqlalchemy.event import listens_for
from sqlalchemy.orm import validates

class CPFTipo(db.TypeDecorator):
    impl = db.String(14)

    def process_bind_param(self, value, dialect):
        if value is not None:
            # Remover caracteres não numéricos do CPF
            value = ''.join(filter(str.isdigit, value))
        return value

    def process_result_value(self, value, dialect):
        return value

    @staticmethod
    def validate_cpf(cpf):
        # validação do cpf
        return True

    @validates('cpf')
    def validate_cpf_column(self, key, cpf):
        if not self.validate_cpf(cpf):
            raise ValueError('CPF inválido')
        return cpf
    

class Bolsista(db.Model):
    __tablename__ = 'bolsistas'

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String, nullable=False)
    cpf = db.Column(CPFTipo, nullable = False)
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


