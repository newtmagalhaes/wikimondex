from flask_restx import Resource

from ..dto import SetupDTO
from ..service.setup import reset_db

api = SetupDTO.api


@api.route('/')
class Setup(Resource):

    @api.response(204, 'Banco de dados resetado')
    def put(self):
        """Derruba e Cria o banco de dados"""
        return reset_db(), 204
