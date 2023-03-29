from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.get('/hola')
def read_root():
    return {"Hola": "Mundo!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/calculadora")
def calculadora(num1: float, num2: float):
    return{'suma' : num1 + num2}
