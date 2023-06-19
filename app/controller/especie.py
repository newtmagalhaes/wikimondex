from flask import abort
from flask_restx import Resource

from.generic_controller import generic_controller,generic_id_controller

from ..dto.especie import EspecieDTO
from ..service.especie import EspecieService

especie_service = EspecieService()
api = EspecieDTO.api

especie = EspecieDTO.especie
especie_input = EspecieDTO.especie_input
especie_filtro = EspecieDTO.especie_filtro

generic_dto={
    'model': especie,
    'model_input': especie_input,
    'model_filter': especie_filtro
}


class EspecieAPI(generic_controller(api,generic_dto,especie_service)):
    pass

class EspecieIdAPI(generic_id_controller(api,generic_dto,especie_service)):
    pass

@api.route('/<int:id>/evolucoes')
@api.param('id','Identificador da entidade')
class EspecieEvolucaoAPI(Resource):
    def get(self, id):
        especie = especie_service.get(id)
        if especie:
            evolucoes = especie.evolutions
            return evolucoes, 200
        abort(404, f"Espécie com ID '{id}' não encontrada.")
