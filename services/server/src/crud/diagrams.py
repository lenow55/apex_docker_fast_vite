import imp
from tortoise.expressions import Q
from tortoise import filters
from typing import List

from src.schemas.records import DiagramRule
from src.schemas.records import DiagramData


async def get_diagrams(rules: List[DiagramRule]): #Тут делаем запрос к базе данных
    return [{'id':8, 'name':"ksdjf", 'series':[5, 10], 'cat_ids':[1, 2], 'categories':["first", "second"]}]