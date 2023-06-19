from sqlalchemy import or_
from ..models import Bolsista, Especie, Especime
from .db_service import DBService

class BolsistaService(DBService):
    
    def __init__(self):
        super().__init__(Bolsista)
    
    def filter_clauses(self, query_params: dict) -> list:
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

    def get_all(self, query_params: dict = {}) -> list:
        query = self.session.query(self.model_class)
        if hasattr(self,'filter_clauses'):
            query = query.join(Especime).join(Especie)
            filter_clauses = self.filter_clauses(query_params)
            query = query.filter(*filter_clauses)
        # print(query)
        return query.all()

    def get_bolsistas_by_especime_tipo(self, type_filter):
        bolsistas = Bolsista.query \
            .join(Especime) \
            .join(Especie) \
            .filter(
                (Especie.primary_type == type_filter) |
                (Especie.secondary_type == type_filter)
            ) \
            .all()
        return bolsistas
