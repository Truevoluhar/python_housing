from pydantic import BaseModel
from typing import Optional, Any

class TestModel(BaseModel):
    flt: Optional[float] = None
    text: Optional[str] = None

testObject = TestModel(flt=123.05, text="asd")

def pydantic_to_response_format(model_cls: type[BaseModel], name: str | None = None) -> dict:
    return {
        "type": "json_schema",
        "json_schema": {
            "name": name or model_cls.__name__,
            "strict": True,
            "schema": model_cls.model_json_schema(),
        },
    }


response_format = pydantic_to_response_format(TestModel)
print(response_format)