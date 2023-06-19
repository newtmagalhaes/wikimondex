from flask_restx import Namespace, fields


class BolsistaDTO:
    api = Namespace('bolsista')

    bolsista_input = api.model(
        'bolsista_input',
        {
            'nome': fields.String(required=True),
            'cpf': fields.String(required=True),
            'data_nascimento': fields.Date(required=True),
            'foto_perfil_filekey': fields.String(description='File Access Key'),
        }
    )

    bolsista = api.clone(
        'bolsista',
        {'id': fields.Integer(readonly = True)},
        bolsista_input,
    )

    bolsista_quantidade_especime= api.model
