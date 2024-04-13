from typing import Any, Dict, List, Optional, Union
from bs4 import BeautifulSoup
from app.handlers.api_handler import ApiHandler
from app.resources.errors import CRASH, NOT_FOUND
from pprint import pprint

api = ApiHandler("https://manganato.com")

async def get_recent_manga() -> Union[Dict[str, Any], int]:
    response: Any = await api.get(endpoint="/genre-all", html=True)
    
    if type(response) is int:
        return CRASH

    soup = get_soup(html=response)
    items: List = soup.select('.content-genres-item')
    mangas: List[Dict[str, Any]] = []

    for item in items:
        chap_ele = item.select('.genres-item-chap.text-nowrap.a-h')[0]
        chap_slug = chap_ele.get("href").replace("https://chapmanganato.to", "")
        chap_name = chap_ele.get("title")
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

    return {
        "mangas": mangas
    }

def get_soup(html) -> BeautifulSoup:
    return BeautifulSoup(html, 'html.parser')