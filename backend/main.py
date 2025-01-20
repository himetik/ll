from fastapi import FastAPI, HTTPException
import httpx
from backend.models import LinkRequest


app = FastAPI()


@app.post("/check-link")
async def check_link(link: LinkRequest):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(link.url, timeout=10)
            return {"url": link.url, "status": response.status_code}
    except httpx.RequestError as e:
        raise HTTPException(status_code=400, detail=f"Error accessing the URL: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
