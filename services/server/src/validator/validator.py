from typing import List, Tuple

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
    column_to_id: List[column2id] = [
        column2id(0, "значение 1", "val_1", "просто булево значение"),
        column2id(1, "значение 2", "val_2", "просто булево значение"),
        column2id(2, "значение 3", "val_3", "просто булево значение"),
        column2id(3, "значение 4", "val_4", "просто булево значение"),
        column2id(4, "значение 5", "val_5", "просто булево значение")
    ]
    cat_to_id: List[cat2id] = [
        cat2id(0, "True"),
        cat2id(1, "False")
    ]

    def serialise(self, diagram):
        name = list(diagram[0])[0]
        dt = [i for i in self.column_to_id if i.db_name == name][0]
        print(dt)
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

    def get_filters(self, rules_list: List[DiagramRule])  -> List[Q]:
        try:
            rules_list = list(set(rules_list))
        except TypeError:
            pass

        query: List[Q] = []
        try:
            for rule in rules_list:
                dt = [i for i in self.column_to_id if i.id == rule.id_diagram][0]
                for index in rule.exclude_fields_id:
                    cat_name = [i for i in self.cat_to_id if i.id == index]
                    query.append(~Q(**{dt.db_name: bool(cat_name)}))
        except:
            pass

        return query
