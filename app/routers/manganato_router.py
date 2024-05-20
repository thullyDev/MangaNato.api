from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.handlers.response_handler import ResponseHandler
from app.resources.errors import CRASH
from typing import Any, Dict, Optional, Union
from app.routers.manganato.manganato import (
     get_filter_mangas, 
     get_top_mangas, 
     get_search_mangas, 
     get_manga,
     get_panels,
     download_image_from_url,
)
from fastapi.responses import FileResponse, StreamingResponse

router: APIRouter = APIRouter(prefix="/manga")
response: ResponseHandler = ResponseHandler()

@router.get("/proxy/{image_url:path}")
def proxy(image_url: Optional[str] = None):
     image_bytes = download_image_from_url(image_url)

     if not image_bytes:
          return FileResponse("media/error.gif", media_type="image/gif")

     return StreamingResponse(iter([image_bytes]), media_type="image/jpeg")


@router.get("/filter")
async def filter_mangas(
     genre: Optional[str] = "genre-all", 
     page: Optional[str] = "", 
     status: Optional[str] = None, 
     _type: Optional[str] = "topview", 
     ) -> JSONResponse:
     params = { "type": _type }
     if status:
          params["state"] = status
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint=f"/{genre}/{page}", params=params)
     if data == CRASH:
          return response.bad_request_response()

     return response.successful_response({"data": data })

@router.get("/recent")
async def recent_mangas(page: Optional[str] = "") -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint=f"/genre-all/{page}")
     return response.successful_response({"data": data })

@router.get("/popular")
async def popular_mangas(page: Optional[str] = "") -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint=f"/genre-all/{page}", params={"type": "topview"})
     return response.successful_response({"data": data })

@router.get("/newest")
async def newest_mangas(page: Optional[str] = "") -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint=f"/genre-all/{page}", params={"type": "newest"})
     return response.successful_response({"data": data })

@router.get("/complete")
async def complete_mangas(page: Optional[str] = "") -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint=f"/genre-all/{page}", params={"state": "completed", "type": "topview"})
     return response.successful_response({"data": data })


@router.get("/ongoing")
async def ongoing_mangas(page: Optional[str] = "") -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint=f"/genre-all/{page}", params={"state": "ongoing", "type": "topview"})
     return response.successful_response({"data": data })

@router.get("/genres/{genre}/")
async def genre_mangas(genre: int, page: Optional[str] = "") -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_filter_mangas(endpoint=f"/{genre}/{page}", params={"type": "topview"})
     if data == CRASH:
          return response.bad_request_response()

     return response.successful_response({"data": data })

@router.get("/search/{query}")
async def search_mangas(query: str, page: Optional[str] = "1") -> JSONResponse:
     data: Union[Dict[str, Any], int] = await get_search_mangas(endpoint=f"/search/story/{query}", params={"page": page})

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


