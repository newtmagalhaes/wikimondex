from typing import List

from .dbService import DBService
from ..models.bolsista import Bolsista

class BolsistaService(DBService):
    
    def __init__(self) :
        super().__init__(Bolsista)

