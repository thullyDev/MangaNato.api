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
- **Description:** Get recent mangas.
- **Response:** Returns recent mangas data.

```json
{
  "data": {
    "mangas": [
      {
        "title": "Villain Classroom",
        "image_url": "https://avt.mkklcdnv6temp.com/17/k/34-1711598179.jpg",
        "description": "Heo Jeong-woo, a high school student who is bullied by a girl in his class for his weakness.Han Bo-ra, a transfer student, comes to Jeong-woo's class, where he was spending his miserable days.Jeong-woo feels a strong sense of déjà vu when he sees the child with straight black hair and stains on his legs. Sure enough, Han Bo-ra, who has subdued the arguing classmates, asks them.\"'Have y",
        "slug": "/manga-yp1001450",
        "chapter": {
          "slug": "/manga-yp1001450/chapter-4",
          "name": "Villain Classroom Chapter 4: Chapter 4"
        },
        "views": "20.4K",
        "author": "Jooho",
        "update": "Apr 16,24",
        "score": "4.7"
      }
    ]
  },
  "status_code": 200,
  "message": "sucessful"
}
```

### Get Popular Mangas

- **URL:** `/popular`
- **Method:** GET
- **Description:** Get popular mangas.
- **Response:** Returns popular mangas data.

```json
{
  "data": {
    "mangas": [
      {
        "title": "Villain Classroom",
        "image_url": "https://avt.mkklcdnv6temp.com/17/k/34-1711598179.jpg",
        "description": "Heo Jeong-woo, a high school student who is bullied by a girl in his class for his weakness.Han Bo-ra, a transfer student, comes to Jeong-woo's class, where he was spending his miserable days.Jeong-woo feels a strong sense of déjà vu when he sees the child with straight black hair and stains on his legs. Sure enough, Han Bo-ra, who has subdued the arguing classmates, asks them.\"'Have y",
        "slug": "/manga-yp1001450",
        "chapter": {
          "slug": "/manga-yp1001450/chapter-4",
          "name": "Villain Classroom Chapter 4: Chapter 4"
        },
        "views": "20.4K",
        "author": "Jooho",
        "update": "Apr 16,24",
        "score": "4.7"
      }
    ]
  },
  "status_code": 200,
  "message": "sucessful"
}
```

### Get Newest Mangas

- **URL:** `/newest`
- **Method:** GET
- **Description:** Get newest mangas.
- **Response:** Returns newest mangas data.

```json
{
  "data": {
    "mangas": [
      {
        "title": "Villain Classroom",
        "image_url": "https://avt.mkklcdnv6temp.com/17/k/34-1711598179.jpg",
        "description": "Heo Jeong-woo, a high school student who is bullied by a girl in his class for his weakness.Han Bo-ra, a transfer student, comes to Jeong-woo's class, where he was spending his miserable days.Jeong-woo feels a strong sense of déjà vu when he sees the child with straight black hair and stains on his legs. Sure enough, Han Bo-ra, who has subdued the arguing classmates, asks them.\"'Have y",
        "slug": "/manga-yp1001450",
        "chapter": {
          "slug": "/manga-yp1001450/chapter-4",
          "name": "Villain Classroom Chapter 4: Chapter 4"
        },
        "views": "20.4K",
        "author": "Jooho",
        "update": "Apr 16,24",
        "score": "4.7"
      }
    ]
  },
  "status_code": 200,
  "message": "sucessful"
}
```

### Get Complete Mangas

- **URL:** `/complete`
- **Method:** GET
- **Description:** Get complete mangas.
- **Response:** Returns complete mangas data.

```json
{
  "data": {
    "mangas": [
      {
        "title": "Villain Classroom",
        "image_url": "https://avt.mkklcdnv6temp.com/17/k/34-1711598179.jpg",
        "description": "Heo Jeong-woo, a high school student who is bullied by a girl in his class for his weakness.Han Bo-ra, a transfer student, comes to Jeong-woo's class, where he was spending his miserable days.Jeong-woo feels a strong sense of déjà vu when he sees the child with straight black hair and stains on his legs. Sure enough, Han Bo-ra, who has subdued the arguing classmates, asks them.\"'Have y",
        "slug": "/manga-yp1001450",
        "chapter": {
          "slug": "/manga-yp1001450/chapter-4",
          "name": "Villain Classroom Chapter 4: Chapter 4"
        },
        "views": "20.4K",
        "author": "Jooho",
        "update": "Apr 16,24",
        "score": "4.7"
      }
    ]
  },
  "status_code": 200,
  "message": "sucessful"
}
```

### Get Ongoing Mangas

- **URL:** `/ongoing`
- **Method:** GET
- **Description:** Get ongoing mangas.
- **Response:** Returns ongoing mangas data.

```json
{
  "data": {
    "mangas": [
      {
        "title": "Villain Classroom",
        "image_url": "https://avt.mkklcdnv6temp.com/17/k/34-1711598179.jpg",
        "description": "Heo Jeong-woo, a high school student who is bullied by a girl in his class for his weakness.Han Bo-ra, a transfer student, comes to Jeong-woo's class, where he was spending his miserable days.Jeong-woo feels a strong sense of déjà vu when he sees the child with straight black hair and stains on his legs. Sure enough, Han Bo-ra, who has subdued the arguing classmates, asks them.\"'Have y",
        "slug": "/manga-yp1001450",
        "chapter": {
          "slug": "/manga-yp1001450/chapter-4",
          "name": "Villain Classroom Chapter 4: Chapter 4"
        },
        "views": "20.4K",
        "author": "Jooho",
        "update": "Apr 16,24",
        "score": "4.7"
      }
    ]
  },
  "status_code": 200,
  "message": "sucessful"
}
```

### Get Genre Mangas

- **URL:** `/genres/{genre}`
- **Method:** GET
- **Description:** Get mangas by genre.
- **Parameters:**
  - `{genre}` (int): Genre ID.
- **Response:** Returns mangas data based on the specified genre.

```json
{
  "data": {
    "mangas": [
      {
        "title": "Villain Classroom",
        "image_url": "https://avt.mkklcdnv6temp.com/17/k/34-1711598179.jpg",
        "description": "Heo Jeong-woo, a high school student who is bullied by a girl in his class for his weakness.Han Bo-ra, a transfer student, comes to Jeong-woo's class, where he was spending his miserable days.Jeong-woo feels a strong sense of déjà vu when he sees the child with straight black hair and stains on his legs. Sure enough, Han Bo-ra, who has subdued the arguing classmates, asks them.\"'Have y",
        "slug": "/manga-yp1001450",
        "chapter": {
          "slug": "/manga-yp1001450/chapter-4",
          "name": "Villain Classroom Chapter 4: Chapter 4"
        },
        "views": "20.4K",
        "author": "Jooho",
        "update": "Apr 16,24",
        "score": "4.7"
      }
    ]
  },
  "status_code": 200,
  "message": "sucessful"
}
```

### Search Mangas

- **URL:** `/search/{query}`
- **Method:** GET
- **Description:** Search for mangas.
- **Parameters:**
  - `{query}` (str): Search query.
- **Response:** Returns search results.

```json
{
  "data": {
    "mangas": [
      {
        "title": "Villain Classroom",
        "image_url": "https://avt.mkklcdnv6temp.com/17/k/34-1711598179.jpg",
        "description": "Heo Jeong-woo, a high school student who is bullied by a girl in his class for his weakness.Han Bo-ra, a transfer student, comes to Jeong-woo's class, where he was spending his miserable days.Jeong-woo feels a strong sense of déjà vu when he sees the child with straight black hair and stains on his legs. Sure enough, Han Bo-ra, who has subdued the arguing classmates, asks them.\"'Have y",
        "slug": "/manga-yp1001450",
        "chapter": {
          "slug": "/manga-yp1001450/chapter-4",
          "name": "Villain Classroom Chapter 4: Chapter 4"
        },
        "views": "20.4K",
        "author": "Jooho",
        "update": "Apr 16,24",
        "score": "4.7"
      }
    ]
  },
  "status_code": 200,
  "message": "sucessful"
}
```
### Get Top Mangas

- **URL:** `/top`
- **Method:** GET
- **Description:** Get top mangas.
- **Response:** Returns top mangas data.

```json
{
  "data": {
    "mangas": [
      {
        "title": "Villain Classroom",
        "image_url": "https://avt.mkklcdnv6temp.com/17/k/34-1711598179.jpg",
        "description": "Heo Jeong-woo, a high school student who is bullied by a girl in his class for his weakness.Han Bo-ra, a transfer student, comes to Jeong-woo's class, where he was spending his miserable days.Jeong-woo feels a strong sense of déjà vu when he sees the child with straight black hair and stains on his legs. Sure enough, Han Bo-ra, who has subdued the arguing classmates, asks them.\"'Have y",
        "slug": "/manga-yp1001450",
        "chapter": {
          "slug": "/manga-yp1001450/chapter-4",
          "name": "Villain Classroom Chapter 4: Chapter 4"
        },
        "views": "20.4K",
        "author": "Jooho",
        "update": "Apr 16,24",
        "score": "4.7"
      }
    ]
  },
  "status_code": 200,
  "message": "sucessful"
}
```

### Get Manga Details

- **URL:** `/{manga_id}`
- **Method:** GET
- **Description:** Get details of a manga.
- **Parameters:**
  - `{manga_id}` (str): Manga ID.
- **Response:** Returns manga details.

```json
{
  "data": {
    "manga": {
      "manga_id": "manga-sh995616",
      "image_url": "https://avt.mkklcdnv6temp.com/33/d/1-1583464999.jpg",
      "title": "The Cool Classmate ◯◯ Years Later...",
      "alt_names": "The Cool Classmate XX Years Later... ; Cool na Doukyuusei no ◯◯ Nengo… ; クールな同級生の◯◯年後... ; The Cool Classmate ◯◯ Years Later...",
      "status": "Ongoing",
      "description": "The cool classmate ◯◯ years later... summary is updating. Come visit MangaNato.com sometime to read the latest chapter of The cool classmate ◯◯ years later.... If you have any question about this manga, Please don't hesitate to contact us or translate team. Hope you enjoy it.",
      "genres": [
        {
          "name": "Comedy",
          "slug": "/genre-6"
        },
        {
          "name": "Romance",
          "slug": "/genre-27"
        },
        {
          "name": "Slice of life",
          "slug": "/genre-35"
        }
      ],
      "authors": [
        {
          "name": "Kyutai X",
          "slug": "/fGt5dXRhaV94"
        }
      ],
      "chapters": [
        {
          "name": "The cool classmate ◯◯ years later... Chapter 3",
          "slug": "/chapter-3",
          "views": "86.7K",
          "date": "Apr 14,2023 22:04"
        },
        {
          "name": "The cool classmate ◯◯ years later... Chapter 2",
          "slug": "/chapter-2",
          "views": "98.5K",
          "date": "Apr 14,2023 17:04"
        },
        {
          "name": "The cool classmate ◯◯ years later... Chapter 1",
          "slug": "/chapter-1",
          "views": "102.1K",
          "date": "Apr 14,2023 17:04"
        }
      ]
    }
  },
  "status_code": 200,
  "message": "sucessful"
}
```

### Read Chapter

***!important: you may need to download each url panel and serve it, you do this to bypass the forbidden response***

- **URL:** `/{manga_id}/{chapter_id}`
- **Method:** GET
- **Description:** Read a chapter of a manga.
- **Parameters:**
  - `{manga_id}` (str): Manga ID.
  - `{chapter_id}` (str): Chapter ID.
- **Response:** Returns chapter data.
  
```json
{
  "data": {
    "panels": [
      {
        "image_url": "https://v0.mkklcdnv6tempv2.com/img/tab_20/04/42/59/sh995616/chapter_1/1-o.jpg",
        "title": "The cool classmate ◯◯ years later... Chapter 1 page 1"
      }
    ]
  },
  "status_code": 200,
  "message": "sucessful"
}
```

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
