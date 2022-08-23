from fastapi import APIRouter
from starlette.responses import JSONResponse

import src.crud.records as crud
from src.schemas.records import RecordSchema
from fastapi.responses import ORJSONResponse
from typing import List

router = APIRouter()

# будем сразу делать запрос на все схемы и
# возвращать данные


@router.post(
    "/record", response_model=None
)
async def create_record(
    record: RecordSchema
):
    return await crud.create_record(record)

@router.post(
    "/records", response_model=None
)
async def create_records(
    records: List[RecordSchema]
):
    return await crud.create_records(records)

@router.get(
    "/records", response_model=List[RecordSchema], response_class=ORJSONResponse
)
async def get_records():
    cont = await crud.get_records()
    r = [dict(v) for v in cont]
    return ORJSONResponse(content=r)
