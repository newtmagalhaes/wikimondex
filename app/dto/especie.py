from flask_restx import Namespace, fields
from flask_restx.reqparse import Argument

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
                enum=Poketipo._member_names_,
            ),
            'secondary_type': fields.String(
                enum=Poketipo._member_names_,
            ),
            'origin_id': fields.Integer(),
        },
        strict=True,
    )

    especie = api.clone(
        'especie',
        {'id': fields.Integer(readonly=True)},
        especie_input,
    )

    especie_filtro = api.parser()
    especie_filtro.add_argument(Argument(
        'texto',
        dest='text',
        type=str,
        location='args',
        store_missing=False,
    ))
    especie_filtro.add_argument(Argument(
        'tipo',
        dest='types',
        type=str,
        location='args',
        store_missing=False,
        action='append',
        choices=Poketipo._member_names_,
        help=f'Possíveis valores: {Poketipo._member_names_}',
    ))

    wild_count = fields.Wildcard(
        fields.Integer,
        readonly=True,
        description="Quantidade contada.",
    )
    especie_contada = api.model(
        'especie_contada',
        {'*': wild_count},
    )

