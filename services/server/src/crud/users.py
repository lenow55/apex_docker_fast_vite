from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.database.models import Records
from schemas.records import RecordSchema




async def create_record(user) -> RecordSchema:

    try:
        user_obj = await Records.create(**user.dict(exclude_unset=True))
    except Exception:
        raise HTTPException(status_code=400, detail=f"Произошла какая-то ошибка")

    return await RecordSchema.from_tortoise_orm(user_obj)


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

async def query_field(user) -> RecordSchema: