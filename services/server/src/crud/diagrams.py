import imp
from tortoise.expressions import Q, Expression
from tortoise import filters
from tortoise.functions import Count
from typing import List, Tuple

from src.schemas.records import RecordSchema
from src.schemas.records import CategoriesRecordSchema
from src.database.models import Records
from src.schemas.diagram import DiagramRule
from src.schemas.diagram import DiagramData
from src.validator.validator import Validator


async def get_diagrams(rules: List[DiagramRule]):  # Тут делаем запрос к базе данных
    validator = Validator()
    data_diagrams = []
    filters_list = validator.get_filters(rules=rules)
    try:
        for column in validator.get_fields():
            data_diagrams.append(
                await Records
                .filter(Q(*filters_list, join_type='AND'))
                .annotate(count=Count(column))
                .group_by(column)
                .values(column, "count"))
    except Exception as ex:
        print(ex)
    print(data_diagrams)
    out_diagrams_data: List[DiagramData] = []
    for diagram in data_diagrams:
        out_diagrams_data.append(validator.serialise(diagram))
    return out_diagrams_data
