import imp
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app =  FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

data = [
    {
        "id":1,
        "price":45,
        "name":"mat"
    },
    {
        "id":2,
        "price":450,
        "name":"watch"
    },
    {
        "id":1,
        "price":100,
        "name":"knife"
    },
    {
        "id":1,
        "price":201,
        "name":"clock"
    }
]
@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.post("/item")
async  def get_item(item:Item):
    return item

@app.get("/items/{item_id}")
async  def read_item(item_id:float):
    return {"item_id": item_id}

@app.get("/items/")
async  def read_item(skip:int,limit:int):
    return data[skip:skip+limit]

