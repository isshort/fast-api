from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

db = []


class City(BaseModel):
    name: str
    timezone: str


@app.get('/')
def index():
    return {"name": "Namatullah", "surname": "Wahidi"}


@app.get("/cites")
def get_cities():
    return db


@app.post("/cite")
def create_city(city: City):
    db.append(city.dict())
    return db[-1]


@app.get("/city_id")
def get_city(city_id: int):
    return db[city_id - 1]


@app.delete("/city_id")
def delete_city(city_id: int):
    db.pop(city_id - 1)
    return {}
