from .generic_db_service import GenericDBService
from ..db import db

class DBService(GenericDBService):
    def __init__(self, model_class):
        super().__init__(db.session, model_class)
