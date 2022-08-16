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
    column_to_id: List[column2id] = [
        column2id(0, "разрешено/запрещено", "blocked_acess", "отношение заблокированных и разрешённых ресурсов"),
        column2id(1, "Возраст", "age_limit", "Возрастное ограничение"),
        column2id(2, "Темы", "theam_restriction", "Ограничение по темам"),
    ]
    cat_to_id: List[cat2id] = [
        cat2id(0, "Разрешено"),
        cat2id(1, "Запрещено"),
        cat2id(2, "0+"),
        cat2id(3, "6+"),
        cat2id(4, "12+"),
        cat2id(5, "16+"),
        cat2id(6, "18+"),
        cat2id(7, "Бизнес"),
        cat2id(8, "Вредоносные сайты"),
        cat2id(9, "Детям"),
        cat2id(10, "Загрузка файлов"),
        cat2id(11, "Здоровье"),
        cat2id(12, "Игры и развлечения"),
        cat2id(13, "Культура"),
        cat2id(14, "Мультимедиа"),
        cat2id(15, "Наука и технологии"),
        cat2id(16, "Ненормативная лексика"),
        cat2id(17, "Новости и СМИ"),
        cat2id(18, "Образование"),
        cat2id(19, "Общество и политика"),
        cat2id(20, "Поисковые системы"),
        cat2id(21, "Пользовательский контент"),
        cat2id(22, "Прокси и анонимайзеры"),
        cat2id(23, "Противоправные сайты"),
        cat2id(24, "Реклама и маркетинг"),
        cat2id(25, "Социальные сети"),
        cat2id(26, "Спорт и хобби"),
        cat2id(27, "Справочная информация "),
        cat2id(28, "Без категории")
    ]

    def serialise(self, diagram):
        name = list(diagram[0])[0]
        dt = [i for i in self.column_to_id if i.db_name == name][0]
        data: List[Data] = []
        for rec in diagram:
            id_categorie = int(rec[name])
            count = rec['count']
            cat = [i for i in self.cat_to_id if i.id == id_categorie][0]
            data.append(Data(id=cat.id, name=cat.name, count=count))

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
                    cat_id = [i.id for i in self.cat_to_id if i.id == index][0]
                    query.append(~Q(**{dt.db_name: cat_id}))
        except:
            pass

        return query
