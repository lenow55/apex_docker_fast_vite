from tortoise.contrib.pydantic.creator import pydantic_model_creator, pydantic_queryset_creator

from src.database.models import Records


RecordSchema = pydantic_model_creator(
    Records, name="Record", exclude_readonly=True
)

RecordQueryMD = pydantic_queryset_creator(
    Records, exclude=tuple(['id'])
)
