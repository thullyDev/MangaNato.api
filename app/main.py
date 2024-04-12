from fastapi import FastAPI
from typing import Any, Dict

app = FastAPI()

@app.get("/")
def root() -> Dict[str, str]:
    return {"Message": "bot is running... follow me on https://github.com/thullDev"}

