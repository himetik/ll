from fastapi import HTTPException
import httpx
from models import StandardResponse, DataResponse, ErrorResponse


def check_url_status(url: str) -> StandardResponse:
    try:
        with httpx.Client() as client:
            response = client.get(url, timeout=5)
            if response.status_code < 400:
                return StandardResponse(
                    success=True,
                    data=DataResponse(status="up", code=response.status_code)
                )
            else:
                return StandardResponse(
                    success=True,
                    data=DataResponse(status="down", code=response.status_code)
                )
    except httpx.RequestError as e:
        return StandardResponse(
            success=False,
            error=ErrorResponse(message="Request failed", details=str(e))
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
