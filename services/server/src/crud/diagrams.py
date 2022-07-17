import imp
from tortoise.expressions import Q
from tortoise import filters
from tortoise.functions import Count
from typing import List

from src.schemas.records import RecordSchema
from src.schemas.records import CategoriesRecordSchema
from src.database.models import Records
from src.schemas.diagram import DiagramRule
from src.schemas.diagram import DiagramData
from src.validator.validator import Validator


async def get_diagrams(rules: List[DiagramRule]):  # Тут делаем запрос к базе данных
    data_diagrams = []
    validator = Validator()
    #d_var_1 = DiagramData(
    #    id=1, name="diagram1", series=[],
    #    cat_ids=[],
    #    categories=["positive", "negative"])
    filters_list = []
    filters_list = [Q(val_1=True), Q(val_2=False)]
    try:
        for field in CategoriesRecordSchema.__fields__.keys():
            data_diagrams.append(
                await Records
                .filter(Q(*filters_list, join_type='AND'))
                .annotate(count=Count(field))
                .group_by(field)
                .values(field, "count"))
    except Exception as ex:
        print(ex)
    print(data_diagrams)
    out_diagrams_data: List[DiagramData] = []
    i = 0
    for diagram in data_diagrams:
        out_diagrams_data.append(validator.serialise(diagram))
    return out_diagrams_data
