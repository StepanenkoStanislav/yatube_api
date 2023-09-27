# Yatube API - API for YaTube
## Описание
Сервис Yatube API позволяет приложениям взаимодействовать с yatube.<br>
Для авторизации пользователей используется аутентификация по токену.
Неаутентифицированные пользователи могут только просматривать группы, посты, 
а также комментарии к ним. Аутентифицированные пользователи могут также 
создавать и редактировать свои посты и комментарии, а также подписываться на 
других пользователей.

## Установка

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов

### GET /api/v1/posts/
#### Parameters
`limit (Количество постов на странице.)`<br>
`offset (Индекс поста с которого начнут выводиться результаты.)`
#### Response
`HTTP Status 200`
```
{
  "count": 123,
  "next": "http://127.0.0.1:8000/api/v1/posts/?offset=400&limit=100",
  "previous": "http://127.0.0.1:8000/api/v1/posts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2023-03-10T07:41:00.460Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### POST /api/v1/posts/
#### Parametrs
`No parameters`
#### Request body
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
#### Response
`HTTP Status 201`
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2023-03-11T07:41:00.390Z",
  "image": "string",
  "group": 0
}
```

## Технологии

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="python" alt="python" width="40" height="40"/>&nbsp
  <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="django" alt="django" width="40" height="40"/>&nbsp
</div>

В проекте используются следующие технологии:
- Python 3.7
- Django 3.2
- DjangoRestFramework 3.12.4

## Автор

[![Telegram Badge](https://img.shields.io/badge/StepanenkoStanislav-blue?logo=telegram&logoColor=white)](https://t.me/tme_zoom) [![Gmail Badge](https://img.shields.io/badge/-Gmail-red?style=flat&logo=Gmail&logoColor=white)](mailto:stepanenko.s.a.dev@gmail.com)
