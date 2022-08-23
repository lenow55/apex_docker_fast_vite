import orjson
from pydantic import BaseModel
from pydantic.schema import schema


class Foo(BaseModel):
    a: int


class Model(BaseModel):
    a: Foo


# Default location for OpenAPI
top_level_schema = schema([Model])
print(orjson.dumps(top_level_schema))
