from fastapi import FastAPI, HTTPException
import httpx
from backend.models import StandardResponse, DataResponse, ErrorResponse


app = FastAPI()


@app.get("/check/", response_model=StandardResponse)
async def check_server(url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5)

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
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )
