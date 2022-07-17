from typing import List
from src.schemas.diagram import DiagramData, DiagramRule

class column2id():
    id: int
    name: str
    description: str
    db_name: str
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
    column_to_id = []
    cat_to_id = []
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
        data = []
        for rec in diagram:

        
            return DiagramData(
                id=i, name=list(diagram[0])[0],
                series=[rec['count'] for rec in diagram],
                cat_ids=[1, 2],
                categories=["first", "second"]))
