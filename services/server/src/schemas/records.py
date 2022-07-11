from tortoise.contrib.pydantic.creator import pydantic_model_creator

from pydantic import BaseModel, Field
from typing import List
from src.database.models import Records


RecordSchema = pydantic_model_creator(
    Records, name="Record", exclude_readonly=True
)

class DiagramData(BaseModel):
    id: int
    name: str
    series: List[int]
    cat_ids: List[int]
    categories: List[str]

class DiagramRule(BaseModel):
    id_diagram: int = Field(ge=0, description="The id must be >= 0")
    include_fields_id: List[int] = Field(ge=0, description="The id must be >= 0")
    # exclude_fields_id: List[int] = Field(gt=0, description="The id must be greater than zero")
