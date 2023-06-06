from flask_restx import Resource

from ..dto.especie import EspecieDTO
from ..service.especie import create_especie

api = EspecieDTO.api
especie_input = EspecieDTO.especie_input
especie = EspecieDTO.especie

@api.route('/')
class EspecieAPI(Resource):
    @api.expect(especie_input, validate=True)
    @api.marshal_with(especie, code=201)
    def post(self):
        data = api.payload
        return create_especie(data), 201
