from fastapi import FastAPI
from typing import Union
import db


app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello: world!"}

@app.get("/items/{items_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/names")
def read_names():
    return db.read_name()