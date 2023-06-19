from .generic_controller import generic_controller,generic_id_controller
from ..dto.bolsista import BolsistaDTO
from ..service.bolsista import BolsistaService

bolsista_input = BolsistaDTO.bolsista_input
bolsista = BolsistaDTO.bolsista

bolsista_service = BolsistaService()
api = BolsistaDTO.api

generic_dto = {
    "model" : bolsista,
    "model_input" : bolsista_input
}

class BolsistaAPI(generic_controller(api, generic_dto, bolsista_service)):
    pass

class BolsistaIdAPI(generic_id_controller(api, generic_dto, bolsista_service)):
    pass

