from flask_restx import Namespace, fields

class EspecimeDTO:
    api = Namespace('especime')

    especime_input = api.model(
        'especime_input',
        {
            'apelido': fields.String(required=True),
            'altura': fields.Float(required=True),
            'peso': fields.Float(required=True),
            'id_bolsista': fields.Integer(required=True),
            'id_especie': fields.Integer(required = True),
            'data_cadastro': fields.Date(required=True),
            'id_capa_especime': fields.Integer(required=True)
        }
    )

    especime = api.clone(
        'especime',
        {'id': fields.Integer(readonly = True)},
        especime_input,
    )

    input_model=especime_input
    output_model = especime