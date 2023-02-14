from typing import List
from fastapi import Response

from tortoise.expressions import Q
from src.database.models import ColumnsId, Acess, AgeLimit, TheamRestriction
from src.schemas.diagram import Data, DiagramData, DiagramRule


class cat2id():
    id: int
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name


class column2id():
    id: ColumnsId
    name: str
    db_name: str
    description: str
    values: list[cat2id]

    def __init__(self, id, name, db_name, description, values):
        self.id = id
        self.name = name
        self.db_name = db_name
        self.description = description
        self.values = values


class Validator():
    column_to_id: List[column2id] = [
        column2id(
            ColumnsId.BLOCKED_ACESS, "разрешено/запрещено", "blocked_acess",
            "отношение заблокированных и разрешённых ресурсов", [
                cat2id(Acess.ALLOW._value_, "Разрешено"),
                cat2id(Acess.DENY._value_, "Запрещено")
            ]
        ),
        column2id(
            ColumnsId.AGE_LIMIT, "Возраст", "age_limit", "Возрастное ограничение",
            [
                cat2id(AgeLimit.NULL.value, "0+"),
                cat2id(AgeLimit.SIX._value_, "6+"),
                cat2id(AgeLimit.TWELVE._value_, "12+"),
                cat2id(AgeLimit.SIXTEEN._value_, "16+"),
                cat2id(AgeLimit.XXX._value_, "18+")
            ]
        ),
        column2id(
            ColumnsId.THEAM_RESTRICTION, "Темы", "theam_restriction", "Ограничение по темам",
            [
                cat2id(TheamRestriction.BUSINESS.value, "Бизнес"),
                cat2id(TheamRestriction.MALICIOUS_SITE._value_, "Вредоносные сайты"),
                cat2id(TheamRestriction.FOR_CHILD._value_, "Детям"),
                cat2id(TheamRestriction.FILE_DOWNLOAD._value_, "Загрузка файлов"),
                cat2id(TheamRestriction.HEALTH._value_, "Здоровье"),
                cat2id(TheamRestriction.GAME_ENTERTAINMENT._value_, "Игры и развлечения"),
                cat2id(TheamRestriction.CULTURE._value_, "Культура"),
                cat2id(TheamRestriction.MULTIMEDIA._value_, "Мультимедиа"),
                cat2id(TheamRestriction.SCIENCE_AND_TECHNOLOGY._value_, "Наука и технологии"),
                cat2id(TheamRestriction.PROFANITY._value_, "Ненормативная лексика"),
                cat2id(TheamRestriction.NEWS_AND_MEDIA._value_, "Новости и СМИ"),
                cat2id(TheamRestriction.EDUCATION._value_, "Образование"),
                cat2id(TheamRestriction.SOCIETY_AND_POLITICS._value_, "Общество и политика"),
                cat2id(TheamRestriction.SEARCH_ENGINES._value_, "Поисковые системы"),
                cat2id(TheamRestriction.USER_CONTENT._value_, "Пользовательский контент"),
                cat2id(TheamRestriction.PROXIES_AND_ANONYMIZERS._value_, "Прокси и анонимайзеры"),
                cat2id(TheamRestriction.ILLEGAL_WEBSITES._value_, "Противоправные сайты"),
                cat2id(TheamRestriction.ADVERTISING_AND_MARKETING._value_, "Реклама и маркетинг"),
                cat2id(TheamRestriction.SOCIAL_NETWORKS._value_, "Социальные сети"),
                cat2id(TheamRestriction.SPORTS_AND_HOBBIES._value_, "Спорт и хобби"),
                cat2id(TheamRestriction.BACKGROUND_INFORMATION._value_, "Справочная информация "),
                cat2id(TheamRestriction.NON_THEAM._value_, "Без категории")
            ]
        )
    ]

    def serialise(self, diagram):
        # print(diagram)
        name = list(diagram[0][0])[0]
        col_id = diagram[1]
        # print(name)
        # print(col_id)
        data: List[Data] = []

        try:
            # dt = [i for i in self.column_to_id if i.db_name == name][0]
            dt = self.column_to_id.__getitem__(col_id)
            # print(dt.id)
            for rec in diagram[0]:
                id_categorie = rec[name]
                # тут может возникнуть ошибка
                # print(id_categorie)
                count = rec['count']
                cat = dt.values.__getitem__(id_categorie)
                data.append(Data(id=cat.id, name=cat.name, count=count))
        except Exception as ex:
            ex.args = "serialise: ", *ex.args
            raise

        return DiagramData(
            id=dt.id, name=dt.name, description=dt.description, data=data
        )

    def get_fields(self):
        return ((i.db_name, i.id) for i in self.column_to_id)

    def get_filters(self, rules_list: List[DiagramRule]) -> List[Q]:
        # print("фильтр")
        if rules_list == None:
            return []
        query: List[Q] = []
        # print(rules_list)
        try:
            rules_list = list(set(rules_list))
        except TypeError as tper:
            tper.args = "get_filters: type: ", *tper.args
            raise
        # print(rules_list)

        try:
            for rule in rules_list:
                # print(rule)
                dt = self.column_to_id.__getitem__(rule.id_diagram.value)
                # print(dt)
                for index in rule.exclude_fields_id:
                    cat_id = dt.values.__getitem__(index)
                    query.append(~Q(**{dt.db_name: cat_id.id}))
        except Exception as ex:
            ex.args = "get_filters: ", *ex.args
            raise

        return query
