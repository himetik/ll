from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
from backend.converter import convert_json_to_yaml
from backend.models import JsonData


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>ll</title>
        </head>
        <body>
        </body>
    </html>
    """


@app.post("/convert/json-to-yaml/")
async def convert_json_to_yaml_endpoint(json_data: JsonData):
    try:
        # Конвертация JSON в YAML
        yaml_result = convert_json_to_yaml(json_data.dict()['data'])
        return {"yaml": yaml_result}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
