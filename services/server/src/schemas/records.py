from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Records


RecordSchema = pydantic_model_creator(
    Records, name="Record", exclude_readonly=True
)

