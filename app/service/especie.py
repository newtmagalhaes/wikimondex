from sqlalchemy import or_

from ..models.especie import Especie
from .db_service import DBService

class EspecieService(DBService):

    def __init__(self):
        super().__init__(Especie)

    def filter_clauses(self,query_params: dict) -> list:
        clauses = []

        if types := query_params.get('types'):
            clauses.append(or_(
                Especie.primary_type.in_(types),
                Especie.secondary_type.in_(types),
            ))

        if text := query_params.get('text'):
            clauses.append(or_(
                Especie.name.ilike(f'%{text}%'),
                Especie.description.ilike(f'%{text}%')
            ))

        return clauses
