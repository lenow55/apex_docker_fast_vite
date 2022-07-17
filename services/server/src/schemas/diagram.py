from pydantic import BaseModel, Field
from typing import List

class Data(BaseModel):
    id: int
    name: str
    count: int

class DiagramData(BaseModel):
    id: int
    name: str
    description: str
    data: List[Data]

class DiagramRule(BaseModel):
    id_diagram: int = Field(ge=0, description="The id must be >= 0")
    include_fields_id: List[int] = Field(ge=0, description="The id must be >= 0")
    # exclude_fields_id: List[int] = Field(gt=0, description="The id must be greater than zero")
