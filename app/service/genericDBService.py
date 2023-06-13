from typing import List
from sqlalchemy.orm import Session

class GenericDBService:

    def __init__(self, session: Session, model_class):
        self.session = session;
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
        obj = self.session.query(self.model_class).get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            self.commit(obj)
        return obj

    def get(self, obj_id: int):
        obj = self.session.query(self.model_class).get(obj_id)
        return obj

    def get_all(self) -> List:
        objs = self.session.query(self.model_class).all()
        return objs
    
    def delete(self,obj_id : int):
        obj = self.session.query(self.model_class).get(obj_id)
        if obj:
            self.session.delete(obj)
            self.commit()
            return True
        return False
