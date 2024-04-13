from pprint import pprint
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.handlers.response_handler import ResponseHandler
from app.resources.errors import CRASH, NOT_FOUND
from typing import Any, Dict, List, Union
from app.routers.manganato.manganato import get_recent_manga

router: APIRouter = APIRouter(prefix="/manga")
response: ResponseHandler = ResponseHandler()

@router.get("/recent")
async def recent_mangas() -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_recent_manga()
     return response.successful_response({"data": data })


