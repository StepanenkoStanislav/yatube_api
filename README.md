# ApiYatube - api for yatube
## Описание
Проект api_yatube позволяет приложениям взаимодействовать с yatube.<br>
Для авторизации пользователей используется аутентификация по токену.
Неаутентифицированные пользователи могут только просматривать группы, посты, 
а также комментарии к ним. Аутентифицированные пользователи могут также 
создавать и редактировать свои посты и комментарии, а также подписываться на 
других пользователей.

## Установка

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/diso-rgb/api_final_yatube.git
```

```
cd api_final_yatube
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
