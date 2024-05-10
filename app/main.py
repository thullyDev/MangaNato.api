from fastapi import FastAPI
from typing import Any, Dict
from .routers import manganato_router 

app = FastAPI()

@app.get("/")
def root() -> Dict[str, str]:
    return {"Message": "server is running... follow me on https://github.com/thullDev"}

app.include_router(manganato_router.router)
