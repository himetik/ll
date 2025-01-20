from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
from backend.converter import convert_json_to_yaml, convert_yaml_to_json
from backend.models import JsonData, YamlData


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
        yaml_result = convert_json_to_yaml(json_data.dict()['data'])
        return {"yaml": yaml_result}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@app.post("/convert/yaml-to-json/")
async def convert_yaml_to_json_endpoint(yaml_data: YamlData):
    try:
        json_result = convert_yaml_to_json(yaml_data.data)
        return {"json": json_result}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
