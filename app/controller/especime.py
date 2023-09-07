from flask_restx import Resource

from .generic_controller import generic_controller,generic_id_controller

from ..dto.especime import EspecimeDTO
from ..service.especime import EspecimeService

especime_service = EspecimeService()
api = EspecimeDTO.api
especime_input = EspecimeDTO.especime_input
especime = EspecimeDTO.especime

generic_dto = {
    'model': especime,
    'model_input': especime_input
}

class EspecimesAPI(generic_controller(api,generic_dto,especime_service)):
    pass

class EspecimeAPI(generic_id_controller(api,generic_dto,especime_service)):
    pass
