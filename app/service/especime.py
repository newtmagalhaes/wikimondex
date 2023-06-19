from typing import List

from .db_service import DBService
from ..models.especime import Especime

class EspecimeService(DBService):
    
    def __init__(self) :
        super().__init__(Especime)
