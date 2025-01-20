from pydantic import BaseModel
from typing import Any


class JsonData(BaseModel):
    data: Any


class YamlData(BaseModel):
    data: str
