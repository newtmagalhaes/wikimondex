from flask_restx import Resource

from ..dto.especime import EspecimeDTO
from ..service.especime import EspecimeService

especimeService = EspecimeService()
api = EspecimeDTO.api
especime_input = EspecimeDTO.especime_input
especime = EspecimeDTO.especime

@api.route('/')
class EspecimesAPI(Resource):

    @api.expect(especime_input, validate=True)
    @api.marshal_with(especime, code=201)
    def post(self):
        data = api.payload
        return especimeService.create(data), 201
    
    @api.marshal_list_with(especime)
    def get(self):
        return especimeService.get_all() , 200

@api.route('/<int:id>')
@api.param('id','Especime identificador')
class EspecimeAPI(Resource):

    @api.marshal_with(especime)
    def get(self,id):
        return especimeService.get(id), 200

    @api.expect(especime_input, validate=True)
    @api.marshal_with(especime)
    def put(self, id):
        data = api.payload
        return especimeService.update(id, data), 200

    @api.response(204, 'Especime deletado com sucesso')
    def delete(self, id):
        if especimeService.delete(id):
            return '', 204
        else:
            return {'message': 'Especime não encontrado'}, 404