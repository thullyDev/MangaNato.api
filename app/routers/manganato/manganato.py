from typing import Any, Dict, List, Optional, Union
from bs4 import BeautifulSoup
from app.handlers.api_handler import ApiHandler
from app.resources.errors import CRASH
import requests

api = ApiHandler("https://manganato.com")
api2 = ApiHandler("https://chapmanganato.to")

async def get_manga(manga_id, **kwargs) -> Union[Dict[str, Any], int]:
    response: Any = await api2.get(**kwargs,  html=True)
    malsync_response: Any = await ApiHandler("https://api.malsync.moe").get(f"/page/MangaNato/{manga_id}")

    if int in [type(response)]:
        return CRASH

    soup: BeautifulSoup = get_soup(response)
    title = soup.select('.story-info-right > h1')[0].text
    description = soup.select('.panel-story-info-description')[0].text.replace("Description :", "").strip()
    alt_names = soup.select('.variations-tableInfo .table-value > h2')[0].text
    status = soup.select('.variations-tableInfo .table-value')[2].text
    link_eles = soup.select('.variations-tableInfo .table-value > .a-h')
    chapter_eles = soup.select('.row-content-chapter > .a-h')
    authors_genres: Dict[str, List[Dict[str, str]]] = {
        "genres": [],
        "authors": [],
        "chapters": [],
    }

    for chapter_ele in chapter_eles:
        link: Any = chapter_ele.select(".chapter-name")[0]
        href: Any = link.get("href").replace(manga_id, "")
        name: Any = link.get("title")
        views: Any = chapter_ele.select(".chapter-view")[0].text
        _date: Any = chapter_ele.select(".chapter-time")[0].get("title")
        slug = href.replace("https://chapmanganato.to/", "").replace("https://manganato.com", "")
        authors_genres["chapters"].append({
            "name": name,
            "slug": slug,
            "views": views,
            "date": _date,
        })

    for link in link_eles:
        href: Any = link.get("href")
        _id = "authors" if "author" in href else "genres"
        name = link.text
        slug = href.replace("https://manganato.com/author/story", "").replace("https://manganato.com", "")
        authors_genres[_id].append({
            "name": name,
            "slug": slug,
        })

    malsync_response = malsync_response if type(malsync_response) is not int else {}   
    image_url = soup.select('.story-info-left .img-loading')[0].get('src')

    return {
        "manga": {
            "manga_id": manga_id,
            "image_url": image_url,
            "title": title,
            "alt_names": alt_names,
            "status": status,
            "description": description,
            **malsync_response,
            **authors_genres
        }
    }

async def get_filter_mangas(**kwargs) -> Union[Dict[str, Any], int]:
    response: Any = await api.get(**kwargs,  html=True)

    if type(response) is int:
        return CRASH

    soup: BeautifulSoup = get_soup(response)
    mangas: List[Dict[str, Any]] = []
    get_filter_page_mangas(html=response, mangas=mangas, soup=soup)

    pagination = get_pagination(soup)

    return {
        "mangas": mangas,
        **pagination,
    }

def get_pagination(soup) -> Dict[str, Dict[str, str]]:
    pageEles = soup.select(".page-blue")
    page = pageEles[0].text.replace("FIRST(", "").replace(")", "")
    pages = pageEles[1].text.replace("LAST(", "").replace(")", "")
    pagination = {
        "pages": pages,
        "page": page,
    }

    return { "pagination": pagination }

async def get_search_mangas(**kwargs) -> Union[Dict[str, Any], int]:
    response: Any = await api.get(**kwargs,  html=True)
    
    if type(response) is int:
        return CRASH

    soup: BeautifulSoup = get_soup(response)
    mangas: List[Dict[str, Any]] = []
    get_search_page_mangas(html=response, mangas=mangas, soup=soup)

    pagination = get_pagination(soup)

    return {
        "mangas": mangas,
        **pagination,
    }

async def get_top_mangas() -> Union[Dict[str, Any], int]:
    response: Any = await api.get(endpoint="/",  html=True)
    
    if type(response) is int:
        return CRASH

    soup = get_soup(response)
    items: List = soup.select('.owl-carousel .item')
    mangas: List[Dict[str, Any]] = []

    for item in items:
        link_ele = item.select('.text-nowrap.a-h')[0]
        title = link_ele.get('title')
        slug = link_ele.get('href').replace("https://manganato.com", "").replace("https://chapmanganato.to", "")
        image_url = item.select('.img-loading')[0].get('src')

        mangas.append({
            "title": title,
            "image_url": image_url,
            "slug": slug,
        })


    return {
        "mangas": mangas
    }

async def get_panels(*, chapter_id, manga_id, **kwargs) -> Union[Dict[str, Any], int]:
    response: Any = await api2.get(**kwargs,  html=True)
    
    if type(response) is int:
        return CRASH

    soup: BeautifulSoup = get_soup(response)
    panel_eles: List = soup.select('.container-chapter-reader > img')
    panels: List[Dict[str, str]] = []
    for panel in panel_eles:
        image_url = panel.get("src")
        title = panel.get("title").replace("- MangaNato.com", "").strip()
        panels.append({
            "image_url": image_url,
            "title": title,
        })

    return {
        "panels": panels,
    }

def get_soup(html) -> BeautifulSoup:
    return BeautifulSoup(html, 'html.parser')

def get_filter_page_mangas(html: str, mangas: List[Dict[str, Any]], soup: BeautifulSoup) -> None:
    items: List = soup.select('.content-genres-item')
    for item in items:
        chap_ele = item.select('.item-chapter.text-nowrap.a-h')
        if not chap_ele:
            chap_ele = item.select('.genres-item-chap.text-nowrap.a-h') 
        chap_ele = chap_ele[0] if chap_ele else {}
        chap_slug = chap_ele.get("href", "").replace("https://chapmanganato.to", "")
        chap_name = chap_ele.get("title", "")
        link_ele = item.select('.genres-item-img.bookmark_check')[0]
        title = link_ele.get('title')
        slug = link_ele.get('href').replace("https://manganato.com", "").replace("https://chapmanganato.to", "")
        description = item.select('.genres-item-description')[0].text.strip()
        author = item.select('.genres-item-author')[0].text
        views = item.select('.genres-item-view')[0].text
        update = item.select('.genres-item-time')[0].text
        score = item.select('.genres-item-rate')[0].text
        image_url = item.select('.img-loading')[0].get('src')

        mangas.append({
            "title": title,
            "image_url": image_url,
            "description": description,
            "slug": slug,
            "chapter": {
                "slug": chap_slug,
                "name": chap_name,
            },
            "views": views,
            "author": author,
            "update": update,
            "score": score,
        })

def get_search_page_mangas(html: str, mangas: List[Dict[str, Any]], soup: BeautifulSoup) -> None:
    items: List = soup.select('.search-story-item')
    for item in items:
        chap_ele = item.select('.item-chapter.text-nowrap.a-h')[0]
        chap_slug = chap_ele.get("href",).replace("https://chapmanganato.to", "")
        chap_name = chap_ele.get("title")
        link_ele = item.select('.item-img.bookmark_check')[0]
        title = link_ele.get('title')
        slug = link_ele.get('href').replace("https://manganato.com", "").replace("https://chapmanganato.to", "")
        author_tag = item.select('.item-author')
        author = author_tag[0].text if author_tag else None
        views = item.select('.item-time')[1].text.replace("View : ", "")
        update = item.select('.item-time')[0].text
        score = item.select('.item-rate')[0].text
        image_url = item.select('.img-loading')[0].get('src')

        mangas.append({
            "title": title,
            "image_url": image_url,
            "slug": slug,
            "chapter": {
                "slug": chap_slug,
                "name": chap_name,
            },
            "views": views,
            "author": author,
            "update": update,
            "score": score,
        })




def download_image_from_url(image_url: Optional[str]) -> Union[None, bytes]:
    if not image_url:
        return None

    headers = {
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'Referer': 'https://chapmanganato.to/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Linux"'
     }

    try:
        response = requests.get(image_url, headers=headers)
        pass
    except Exception as e:
        print(e)
        return None
    else:
        return response.content
