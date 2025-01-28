from datetime import datetime
from fastapi.responses import HTMLResponse
from enum import Enum

from pydantic import BaseModel
from fastapi import FastAPI, Response, HTTPException
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return { "message": "Witaj świecie!"}

@app.get("/weather/simple")
def get_weather_simple():
    return {
        "temperature": 36.6,
        "humidity": 70,
        "timestamp": datetime.now()
    }

@app.get("/xml")
def get_xml():
    title = "Witaj w moim api"
    xml_data = f"""<?xml version="1.0"?>
    <message>
        <title>{title}</title>
        <h1>Witaj Merito!</h1>
        <p>BigData</p>
    </message>
    """
    return Response(content=xml_data, media_type="application/xml")

@app.get("/json")
def get_json():
    return {
        "title": "Witaj w moim api",
        "h1": "Witaj Merito!",
        "p": "BigData"
    }

@app.get("/html", response_class=HTMLResponse)
def get_html():
    return """<!DOCTYPE html>
<html>
    <head>
        <title>Witaj w moim api</title>
    </head>
    <body>
        <h1>Witaj Merito!</h1>
        <p>BigData
    </body>
</html>
    """

class Category(Enum):
    TOOLS = 'tools'
    CONSUMABLES = 'consumables'

class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category

items = {
    0: Item(name='Hammer', price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name='Pliers', price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name='Nails', price=1.99, count=100, id=2, category=Category.CONSUMABLES)
}

@app.get('/items')
def index() -> dict[str, dict[int, Item]]:
    return {'items':items}

@app.get('/items/{item_id}')
def item_id(item_id:int) -> Item:
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f'Item with {item_id=} does not exist.'
        )
    return items[item_id]

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)