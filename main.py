from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"help": "See /docs for more information"}

@app.get("/help")
def help():
    return {"help": "See /docs for more information"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}