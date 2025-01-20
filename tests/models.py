from pydantic import BaseModel


class ErrorResponse(BaseModel):
    message: str
    details: str | None = None


class DataResponse(BaseModel):
    status: str
    code: int


class StandardResponse(BaseModel):
    success: bool
    data: DataResponse | None = None
    error: ErrorResponse | None = None
