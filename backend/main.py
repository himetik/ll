from fastapi import FastAPI, HTTPException
import httpx


app = FastAPI()


@app.get("/check")
async def check_server(url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=6)

        if response.status_code < 400:
            return {"status": "up", "code": response.status_code}
        else:
            return {"status": "down", "code": response.status_code}
    except httpx.RequestError as error:
        return {"status": "down", "error": str(error)}
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(error)}")
