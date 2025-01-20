from fastapi import FastAPI
from backend.models import StandardResponse
from backend.utils import check_url_status


app = FastAPI()


@app.get("/check/", response_model=StandardResponse)
async def check_server(url: str):
    return check_url_status(url)
