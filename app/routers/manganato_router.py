from pprint import pprint
from fastapi import APIRouter, params
from fastapi.responses import JSONResponse
from app.handlers.response_handler import ResponseHandler
from app.resources.errors import CRASH, NOT_FOUND
from typing import Any, Dict, List, Union
from app.routers.manganato.manganato import get_filter_mangas

router: APIRouter = APIRouter(prefix="/manga")
response: ResponseHandler = ResponseHandler()

@router.get("/recent")
async def recent_mangas() -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint="/genre-all")
     return response.successful_response({"data": data })

@router.get("/popular")
async def popular_mangas() -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint="/genre-all", params={"type": "topview"})
     return response.successful_response({"data": data })

@router.get("/newest")
async def newest_mangas() -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint="/genre-all", params={"type": "newest"})
     return response.successful_response({"data": data })


