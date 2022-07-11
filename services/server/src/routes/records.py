from fastapi import APIRouter, HTTPException

import src.crud.records as crud
from src.schemas.records import RecordSchema


router = APIRouter()

# будем сразу делать запрос на все схемы и
# возвращать данные


@router.post(
    "/records", response_model=None
)
async def create_record(
    record: RecordSchema
):
    return await crud.create_record(record)
