from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.post('/')
def read_root():
    return {"Hello: world!"}

@app.post("/items/{items_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}