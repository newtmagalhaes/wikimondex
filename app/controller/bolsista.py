from .generic_controller import generic_controller,generic_id_controller
from ..dto import BolsistaDTO, EspecieDTO
from ..service.bolsista import BolsistaService
from flask_restx import Resource

especie_filtro = EspecieDTO.especie_filtro

bolsista_input = BolsistaDTO.bolsista_input
bolsista = BolsistaDTO.bolsista

bolsista_service = BolsistaService()
api = BolsistaDTO.api

generic_dto = {
    "model" : bolsista,
    "model_input" : bolsista_input,
    'model_filter': especie_filtro,
}

class BolsistaAPI(generic_controller(api, generic_dto, bolsista_service)):
    pass

class BolsistaIdAPI(generic_id_controller(api, generic_dto, bolsista_service)):
    pass

@api.route('/especime_tipo/<string:tipo>')
@api.deprecated
class BolsistaByEspecimeTipo(Resource):
    
    @api.marshal_list_with(BolsistaDTO.bolsista)
    def get(self, tipo):
        return bolsista_service.get_bolsistas_by_especime_tipo(tipo), 200
