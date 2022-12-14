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
    exclude_fields_id: List[int] = Field(ge=0, description="The id must be >= 0")
    # exclude_fields_id: List[int] = Field(gt=0, description="The id must be greater than zero")

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.id_diagram == other.id_diagram and self.exclude_fields_id == other.exclude_fields_id
        return False

    def __hash__(self):
        return hash(self.id_diagram)
