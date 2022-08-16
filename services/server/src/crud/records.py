from fastapi import HTTPException, Response

from src.database.models import Records
from src.schemas.records import RecordSchema

from typing import List


async def create_record(record: RecordSchema) -> Response:

    try:
        await Records.create(**record.dict(exclude_unset=True))
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Произошла какая-то ошибка")

    return Response(status_code=200, content="Sucess")


async def create_records(records: List[RecordSchema]) -> Response:

    try:
        for record in records:
            await Records.create(**record.dict(exclude_unset=True))
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Произошла какая-то ошибка")

    return Response(status_code=200, content="Sucess")
async def get_records() -> List[RecordSchema]:
    try:
        return await RecordSchema.from_queryset(Records.all())
    except Exception:
        raise HTTPException(status_code=400, detail=f"Произошла какая-то ошибка")
