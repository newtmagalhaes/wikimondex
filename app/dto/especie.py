from flask_restx import Namespace, fields

from ..utils.tipos import Poketipo


class EspecieDTO:
    api = Namespace('especie')

    especie_input = api.model(
        'especie_input',
        {
            'name': fields.String(
                required=True
            ),
            'description': fields.String(),
            'primary_type': fields.String(
                required=True,
                enum=Poketipo,
            ),
            'secondary_type': fields.String(
                enum=Poketipo,
            ),
        },
        strict=True,
    )

    especie = api.clone(
        'especie',
        {'id': fields.Integer(readonly=True)},
        especie_input,
    )
