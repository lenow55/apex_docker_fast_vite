from fastapi import APIRouter

import src.crud.records as crud
from src.schemas.records import RecordSchema
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


@router.get(
    "/records", response_model=List[RecordSchema]
)
async def get_records():
    return await crud.get_records()
