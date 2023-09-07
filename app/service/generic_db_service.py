from flask_restx.errors import abort
from sqlalchemy.orm import Session

class GenericDBService:

    def __init__(self, session: Session, model_class):
        self.session = session
        self.model_class = model_class

    def commit(self, *instances):
        try:
            if instances:
                self.session.add_all(instances)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def create(self, data: dict):
        obj = self.model_class(**data)
        self.commit(obj)
        return obj

    def update(self, obj_id: int, data: dict):
        obj = self.get(obj_id)
        for key, value in data.items():
            setattr(obj, key, value)
        self.commit(obj)
        return obj

    def _get(self, obj_id: int):
        return self.session.query(self.model_class).get(obj_id)

    def get(self, obj_id: int):
        if obj := self._get(obj_id):
            return obj
        abort(404, f"Entidade do tipo '{self.model_class.__name__}' não encontrada.")

    def get_all(self, query_params: dict = {}) -> list:
        query = self.session.query(self.model_class)
        if hasattr(self,'filter_clauses'):
            filter_clauses = self.filter_clauses(query_params)
            query = query.filter(*filter_clauses)
        return query.all()


    def delete(self, obj_id: int):
        obj = self.get(obj_id)
        self.session.delete(obj)
        self.commit()
