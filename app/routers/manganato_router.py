from os import kill
from pprint import pprint
from fastapi import APIRouter, params
from fastapi.responses import JSONResponse
from app.handlers.response_handler import ResponseHandler
from app.resources.errors import CRASH, NOT_FOUND
from typing import Any, Dict, List, Optional, Union
from app.routers.manganato.manganato import (
     get_filter_mangas, 
     get_top_mangas, 
     get_search_mangas, 
     get_manga,
     get_panels,
)
import requests

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

@router.get("/complete")
async def complete_mangas() -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint="/genre-all", params={"state": "completed", "type": "topview"})
     return response.successful_response({"data": data })


@router.get("/ongoing")
async def ongoing_mangas() -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint="/genre-all", params={"state": "ongoing", "type": "topview"})
     return response.successful_response({"data": data })

@router.get("/genres/{genre}")
async def genre_mangas(genre: int) -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint=f"/{genre}", params={"type": "topview"})
     if data == CRASH:
          return response.bad_request_response()

     return response.successful_response({"data": data })

@router.get("/search/{query}")
async def search_mangas(query: str) -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_search_mangas(endpoint=f"/search/story/{query}")

     if data == CRASH:
          return response.bad_request_response()

     return response.successful_response({"data": data })

@router.get("/top")
async def top_mangas() -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_top_mangas()
     return response.successful_response({"data": data })

@router.get("/{manga_id}")
async def manga(manga_id: str) -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_manga(endpoint=f"/{manga_id}", manga_id=manga_id)

     if data == CRASH:
          return response.bad_request_response()

     return response.successful_response({"data": data })

@router.get("/{manga_id}/{chapter_id}")
async def read(chapter_id: str, manga_id: str) -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_panels(
          endpoint=f"/{manga_id}/{chapter_id}", 
          manga_id=manga_id, 
          chapter_id=chapter_id
     )

     if data == CRASH:
          return response.bad_request_response()

     return response.successful_response({"data": data })


