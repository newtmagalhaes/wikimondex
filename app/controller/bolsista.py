from flask_restx import Resource

from ..dto.bolsista import BolsistaDTO
from ..service.bolsista import BolsistaService

bolsistaService = BolsistaService()
api = BolsistaDTO.api
bolsista_input = BolsistaDTO.bolsista_input
bolsista = BolsistaDTO.bolsista

@api.route('/')
class BolsistasAPI(Resource):

    @api.expect(bolsista_input, validate=True)
    @api.marshal_with(bolsista, code=201)
    def post(self):
        data = api.payload
        return bolsistaService.create(data), 201
    
    @api.marshal_list_with(bolsista)
    def get(self):
        return bolsistaService.get_all() , 200

@api.route('/<int:id>')
@api.param('id','Bolsista identificador')
class BolsistaAPI(Resource):

    @api.marshal_with(bolsista)
    def get(self,id):
        return bolsistaService.get(id), 200

    @api.expect(bolsista_input, validate=True)
    @api.marshal_with(bolsista)
    def put(self, id):
        data = api.payload
        return bolsistaService.update(id, data), 200

    @api.response(204, 'Bolsista deletado com sucesso')
    def delete(self, id):
        return bolsistaService.delete(id), 204
