from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn1

app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)