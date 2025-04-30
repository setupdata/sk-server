from pydantic import BaseModel
from typing import Any, Optional


class ResponseModel(BaseModel):
    code: int
    msg: str
    data: Optional[Any] = None


def http_ok(data: Any = None) -> ResponseModel:
    return ResponseModel(code=0, msg="", data=data)


def http_err(code: int, msg: str, data: Any = None) -> ResponseModel:
    return ResponseModel(code=code, msg=msg, data=data)
