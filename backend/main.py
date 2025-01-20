from fastapi import FastAPI, HTTPException
import httpx
from backend.models import LinkRequest


app = FastAPI()


@app.post("/check-link")
async def check_link(link: LinkRequest):
    try:
        url_str = str(link.url)
        async with httpx.AsyncClient() as client:
            response = await client.get(url_str, timeout=10)
            return {"url": url_str, "status": response.status_code}
    except httpx.RequestError as e:
        raise HTTPException(status_code=400, detail=f"Error accessing the URL: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
