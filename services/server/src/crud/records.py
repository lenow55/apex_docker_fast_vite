from typing import List

from fastapi import HTTPException, Response
from fastapi.responses import PlainTextResponse

from src.database.models import Records
from src.schemas.records import RecordSchema


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
        raise HTTPException(status_code=400, detail=f"Произошла какая-то ошибка {ex}")

    return Response(status_code=200, content="Sucess")

async def get_records():
    try:
        #model = await RecordQueryMD.from_queryset(Records.all())
        #return model.dict()
        return await Records.all().values(*RecordSchema.__fields__)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=f"Произошла какая-то ошибка {ex}")

async def get_records_len():
    try:
        #model = await RecordQueryMD.from_queryset(Records.all())
        #return model.dict()
        count: int = await Records.all().count()
        return PlainTextResponse(status_code=200, content=f"Количество записей = {count}", media_type="text/plain")
    except Exception:
        raise HTTPException(status_code=400, detail=f"Произошла какая-то ошибка")
