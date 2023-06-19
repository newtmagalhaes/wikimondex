from typing import List

from .db_service import DBService
from ..models.bolsista import Bolsista
from ..models.especie import Especie
from ..models.especime import Especime

class BolsistaService(DBService):
    
    def __init__(self) :
        super().__init__(Bolsista)

    def get_bolsistas_by_especime_tipo (self,type_filter):
        bolsistas = Bolsista.query \
            .join(Especime, Especime.id_bolsista == Bolsista.id) \
            .join(Especie, Especie.id == Especime.id_especie) \
            .filter(
                (Especie.primary_type == type_filter) |
                (Especie.secondary_type == type_filter)
            ) \
            .all()
        return bolsistas
