from typing import List

from tortoise.expressions import Q
from tortoise.functions import Count

from src.database.models import Records
from src.schemas.diagram import DiagramRule
from src.schemas.diagram import DiagramData
from src.validator.validator import Validator

from fastapi import HTTPException, Response


async def get_diagrams(rules: List[DiagramRule]):  # Тут делаем запрос к базе данных
    validator = Validator()
    data_diagrams = []
    out_diagrams_data: List[DiagramData] = []
    # print(rules)
    try:
        filters_list = validator.get_filters(rules_list=rules)
        for column, col_id in validator.get_fields():
            result = await Records.filter(Q(*filters_list, join_type='AND')).annotate(count=Count(column)).group_by(column).values(column, "count")
            if len(result) == 0:
                return Response(status_code=200, content=f"No data by these filters")
            data_diagrams.append((result, col_id))
        # print(data_diagrams)
        for diagram in data_diagrams:
            # print(type(diagram))
            out_diagrams_data.append(validator.serialise(diagram))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Произошла какая-то ошибка, {ex}")
    return out_diagrams_data
