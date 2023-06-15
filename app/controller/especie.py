from flask_restx import Resource

from ..dto.especie import EspecieDTO
from ..service.especie import EspecieService

especieService = EspecieService()
api = EspecieDTO.api
especie_input = EspecieDTO.especie_input
especie = EspecieDTO.especie
especie_filtro = EspecieDTO.especie_filtro


@api.route('/')
class EspeciesAPI(Resource):

    @api.expect(especie_input, validate=True)
    @api.marshal_with(especie, code=201)
    def post(self):
        data = api.payload
        return especieService.create(data), 201

    @api.expect(especie_filtro)
    @api.marshal_list_with(especie)
    def get(self):
        query_params = especie_filtro.parse_args()
        return especieService.get_all(query_param=query_params) , 200

@api.route('/<int:id>')
@api.param('id','Especie identificador')
class EspecieAPI(Resource):

    @api.marshal_with(especie)
    def get(self,id):
        return especieService.get(id), 200

    @api.expect(especie_input, validate=True)
    @api.marshal_with(especie)
    def put(self, id):
        data = api.payload
        return especieService.update(id, data), 200

    @api.response(204, 'Especie deletado com sucesso')
    def delete(self, id):
        return especieService.delete(id), 204
