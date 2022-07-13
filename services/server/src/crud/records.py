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

# async def delete_user(user_id, current_user) -> Status:
#     try:
#         db_user = await RecordSchema.from_queryset_single(Users.get(id=user_id))
#     except DoesNotExist:
#         raise HTTPException(status_code=404, detail=f"User {user_id} not found")

#     if db_user.id == current_user.id:
#         deleted_count = await Users.filter(id=user_id).delete()
#         if not deleted_count:
#             raise HTTPException(status_code=404, detail=f"User {user_id} not found")
#         return Status(message=f"Deleted user {user_id}")

#     raise HTTPException(status_code=403, detail=f"Not authorized to delete")

# async def query_field(user) -> RecordSchema:
