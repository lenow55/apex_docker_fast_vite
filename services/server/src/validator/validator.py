from typing import List

from tortoise.expressions import Q
from src.schemas.diagram import Data, DiagramData, DiagramRule


class column2id():
    id: int
    name: str
    db_name: str
    description: str

    def __init__(self, id, name, db_name, description):
        self.id = id
        self.name = name
        self.db_name = db_name
        self.description = description


class cat2id():
    id: int
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Validator():
    column_to_id: List[column2id]
    cat_to_id: List[cat2id]

    def __init__(self):
        self.column_to_id.append(column2id(1, "значение 1", "val_1", "просто булево значение"))
        self.column_to_id.append(column2id(2, "значение 2", "val_2", "просто булево значение"))
        self.column_to_id.append(column2id(3, "значение 3", "val_3", "просто булево значение"))
        self.column_to_id.append(column2id(4, "значение 4", "val_4", "просто булево значение"))
        self.column_to_id.append(column2id(5, "значение 5", "val_5", "просто булево значение"))

        self.cat_to_id.append(cat2id(1, "True"))
        self.cat_to_id.append(cat2id(2, "False"))

    def serialise(self, diagram):
        name = list(diagram[0])[0]
        dt = [i for i in self.column_to_id if i.name == name][0]
        data: List[Data] = []
        for rec in diagram:
            name_categorie = str(rec[name])
            count = rec['count']
            cat = [i for i in self.cat_to_id if i.name == name_categorie][0]
            data.append(Data(id=cat.id, name=name_categorie, count=count))

        return DiagramData(
            id=dt.id, name=dt.name, description=dt.description, data=data
        )

    def get_fields(self):
        return (i.db_name for i in self.column_to_id)

    def get_filters(self, rules: List[DiagramRule]) -> List[Q]:
        query: List[Q] = []
        for rule in rules:
            dt = [i for i in self.column_to_id if i.id == rule.id_diagram][0]
            query.append(Q({dt.db_name: True}))



