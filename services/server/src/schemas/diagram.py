from pydantic import BaseModel, Field
from typing import List


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
