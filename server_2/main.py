from fastapi import FastAPI #,HTTPException
from pydantic import BaseModel
# from typing import Optional, Dict
import json
from pathlib import Path
import uvicorn


app = FastAPI()
DB_PATH = Path("db/hopping_list.json")



# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float


@app.get("/items")
def get_items():
    return read_db

@app.post("/items")
def create_item(name: str):
    items = read_db()
    new_item = {"id": len(items) + 1, "name": name}
    items.append(new_item)
    write_db(items)
    return new_item


def read_db():
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")


def write_db(data: list):
    return DB_PATH
    



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
