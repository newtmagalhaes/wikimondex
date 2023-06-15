from typing import List

from .dbService import DBService
from ..models.especie import Especie

class EspecieService(DBService):
    
    def __init__(self) :
        super().__init__(Especie)
