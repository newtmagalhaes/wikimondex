from sqlalchemy import or_

from ..models.especie import Especie
from .dbService import DBService


def create_filter_clauses(query_params: dict) -> list:
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


class EspecieService(DBService):

    def __init__(self):
        super().__init__(Especie)

    def get_all(self, query_param: dict = {}) -> list:
        query = self.session.query(self.model_class)

        if filter_clauses := create_filter_clauses(query_param):
            query = query.filter(*filter_clauses)

        return query.all()
