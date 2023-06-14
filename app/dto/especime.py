from flask_restx import Namespace, fields

class EspecimeDTO:
    api = Namespace('especime')

    especime_input = api.model(
        'bolsista_input',
        {
            'apelido': fields.String(required=True),
            'altura': fields.Float(required=True),
            'peso': fields.Float(required=True),
            'data_cadastro': fields.Date(required=True),
        }
    )

    especime = api.clone(
        'especime',
        {'id': fields.Integer(readonly = True)},
        especime_input,
    )

    input_model=especime_input
    output_model = especime