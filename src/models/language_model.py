from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db.languages

    def __init__(self, dict):
        super().__init__(dict)

    # Req. 2
    def to_dict(self):
        return {
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym"),
        }

    # Req. 3
    @classmethod
    def list_dicts(cls):
        data = cls.find()
        return [data.to_dict() for data in data]
