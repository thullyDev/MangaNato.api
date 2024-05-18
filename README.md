# MangaNato.api

## Introduction
This is documentation for a scraper api for [manganato](https://manganato.com/)

## Getting Started
1. ```git clone https://github.com/thullyDev/MangaNato.api.git```
2. ```pip3 install -r requirements.txt``` or ```pip install -r requirements.txt```
3. ```uvicorn app.main:app```

## documentation

## Base URL
```http://127.0.0.1:8000``` or ```http://localhost:8000``` 

All endpoints are prefixed with `/manga`.

## Endpoints

### Get Recent Mangas

- **URL:** `/recent`
- **Method:** GET
- **URL Parameters:**
  - `?page=` (number): page number.
- **Description:** Get recent mangas.
- **Response:** Returns recent mangas data.

### Get Popular Mangas

- **URL:** `/popular`
- **Method:** GET
- **URL Parameters:**
  - `?page=` (number): page number.
- **Description:** Get popular mangas.
- **Response:** Returns popular mangas data.

### Get Newest Mangas

- **URL:** `/newest`
- **Method:** GET
- **URL Parameters:**
  - `?page=` (number): page number.
- **Description:** Get newest mangas.
- **Response:** Returns newest mangas data.

### Get Complete Mangas

- **URL:** `/complete`
- **Method:** GET
- **URL Parameters:**
  - `?page=` (number): page number.
- **Description:** Get complete mangas.
- **Response:** Returns complete mangas data.

### Get Ongoing Mangas

- **URL:** `/ongoing`
- **Method:** GET
- **URL Parameters:**
  - `?page=` (number): page number.
- **Description:** Get ongoing mangas.
- **Response:** Returns ongoing mangas data.

### Get Genre Mangas

- **URL:** `/genres/{genre}`
- **Method:** GET
- **URL Parameters:**
  - `?page=` (number): page number.
- **Description:** Get mangas by genre.
- **Parameters:**
  - `{genre}` (int): Genre ID.
- **Response:** Returns mangas data based on the specified genre.

### Search Mangas

- **URL:** `/search/{query}`
- **Method:** GET
- **URL Parameters:**
  - `?page=` (number): page number.
- **Description:** Search for mangas.
- **Parameters:**
  - `{query}` (str): Search query.
- **Response:** Returns search results.

### Get Top Mangas

- **URL:** `/top`
- **Method:** GET
- **URL Parameters:**
  - `?page=` (number): page number.
- **Description:** Get top mangas.
- **Response:** Returns top mangas data.

### Get Filter Mangas

- **URL:** `/filter`
- **Method:** GET
- **URL Parameters:**
  - `?genre=` (str): type of Genre.
  - `?status=` (str): status of the mangas.
    - ongoing
    - complete
  - `?_type=` (str): type.
    - topview
    - newest
  - `?page=` (number): page number.
- **Description:** Get top mangas.
- **Response:** Returns top mangas data.

### Get Manga Details

- **URL:** `/{manga_id}`
- **Method:** GET
- **Description:** Get details of a manga.
- **Parameters:**
  - `{manga_id}` (str): Manga ID.
- **Response:** Returns manga details.

### Read Chapter

***!important: you may need to download each url panel and serve it, you do this to bypass the forbidden response***

- **URL:** `/{manga_id}/{chapter_id}`
- **Method:** GET
- **Description:** Read a chapter of a manga.
- **Parameters:**
  - `{manga_id}` (str): Manga ID.
  - `{chapter_id}` (str): Chapter ID.
- **Response:** Returns chapter data.
  
## Genres

| name           | slug             |
|----------------|------------------|
| ALL            | genre-all        |
| Action         | genre-2          |
| Adventure      | genre-4          |
| Comedy         | genre-6          |
| Cooking        | genre-7          |
| Doujinshi      | genre-9          |
| Drama          | genre-10         |
| Erotica        | genre-48         |
| Fantasy        | genre-12         |
| Gender bender  | genre-13         |
| Harem          | genre-14         |
| Historical     | genre-15         |
| Horror         | genre-16         |
| Isekai         | genre-45         |
| Josei          | genre-17         |
| Manhua         | genre-44         |
| Manhwa         | genre-43         |
| Martial arts   | genre-19         |
| Mature         | genre-20         |
| Mecha          | genre-21         |
| Medical        | genre-22         |
| Mystery        | genre-24         |
| One shot       | genre-25         |
| Pornographic   | genre-47         |
| Psychological  | genre-26         |
| Romance        | genre-27         |
| School life    | genre-28         |
| Sci fi         | genre-29         |
| Seinen         | genre-30         |
| Shoujo         | genre-31         |
| Shoujo ai      | genre-32         |
| Shounen        | genre-33         |
| Shounen ai     | genre-34         |
| Slice of life  | genre-35         |
| Smut           | genre-36         |
| Sports         | genre-37         |
| Supernatural   | genre-38         |
| Tragedy        | genre-39         |
| Webtoons       | genre-40         |
| Yaoi           | genre-41         |
| Yuri           | genre-42         |

---
Thanks for exploring the Manga API! Feel free to follow for updates and improvements. 😊
