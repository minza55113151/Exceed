from fastapi import FastAPI, Body
from typing import Optional, Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    item_id: int
    item_name: str
    item_bool: bool
    

class ItemDetail(BaseModel):
    item_detail: str = " "

class ItemDetail2(Item, ItemDetail):
    pass

@app.get("/")
def root():
    return {"msg": "welcome to root pages"}


@app.get("/items/{item_id}/{item_name}/{item_bool}")
def show_item(item_id: int = 0, item_name: str = " ", item_bool: bool = None):
    return {"item_id": item_id, "item_name": item_name, "item_bool": item_bool}


# @app.get("/items")
# def show_item_body(item: ItemDetail2):
#     return {"item": item}


@app.get("/items")
def show_item_body(item: Item, item_detail: str = Body()):
    return {"item": item, "item_detail": item_detail}
