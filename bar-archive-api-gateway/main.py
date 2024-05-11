from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from controllers import bar_archive

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/beverage/{beverage_id}")
def get_beverage_by_id(beverage_id: int):
    response = bar_archive.get_beverage_by_id(beverage_id)
    print(response)
    return { "message" : "Hello There !" }
