from fastapi import FastAPI, Query
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()

from enum import Enum


class MyModel(str, Enum):
    firstname = "Namatullah"
    surname = "Wahidi"


@app.get("/models/{model}")
async def get_models(model: MyModel):
    return {"model_name": model.name, "model_value": model.value}


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/more/")
async def read_items_more(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items
