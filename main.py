from typing import Optional

from fastapi import FastAPI
from scripts.mondrian_random import generate_random_mondrian

app = FastAPI()

@app.get("/")
async def root():
    return {"help": "See /docs for more information"}

@app.get("/help")
def help():
    return {"help": "See /docs for more information"}

@app.get("/mondrian")
def mondrian():
    return generate_random_mondrian()