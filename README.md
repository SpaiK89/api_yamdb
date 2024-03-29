# Проект YaMDb

## Описание
Проект YaMDb собирает отзывы пользователей на произведения.
Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

> Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

В каждой категории есть произведения: книги, фильмы или музыка.
Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.

Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).
Новые жанры может создавать только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

### Стек:
```
Python 3.8.6, Django, DRF, PostgreSQL, Simple-JWT.
```

### Запуск проекта:
Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/SpaiK89/api_yamdb
cd api_yamdb
```

Создаем и активируем виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```
для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```
```bash
python -m pip install --upgrade pip
```

Ставим зависимости из requirements.txt:
```bash
pip install -r requirements.txt
```

Переходим в папку api_yamdb:
```bash
cd api_yamdb
```

Выполняем миграции:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

Создаем суперпользователя:
```bash
python manage.py createsuperuser
```

Запускаем проект:
```bash
python manage.py runserver
```

### Документация API YaMDb
Документация доступна по эндпойнту: http://127.0.0.1:8000/redoc/

### Описание доступных эндпоинтов
http://127.0.0.1:8000/api/v1/auth/signup/ - регистрация нового пользователя и/или получение кода подтверждения на указанный адрес электронной почты ('POST')(Не аутентифицированный пользователь)
http://127.0.0.1:8000/api/v1/auth/token/ - получение jwt-токена ('POST') (Не аутентифицированный пользователь)

http://127.0.0.1:8000/api/v1/categories/ - получение списка категорий ('GET')(Не аутентифицированный пользователь), создание новой категории ('POST')(Администратор или суперпользователь)  
http://127.0.0.1:8000/api/v1/categories/{slug}/ - удаление указанной категории ('DELETE')(Администратор или суперпользователь)

http://127.0.0.1:8000/api/v1/genres/ - получение списка жанров ('GET')(Не аутентифицированный пользователь), создание нового жанра ('POST')(Администратор или суперпользователь)   
http://127.0.0.1:8000/api/v1/genres/{slug}/ - удаление указанного жанра ('DELETE')(Администратор или суперпользователь)

http://127.0.0.1:8000/api/v1/titles/ - получение списка всех произведений ('GET')(Не аутентифицированный пользователь), публикация нового произведения ('POST')(Администратор или суперпользователь)  
http://127.0.0.1:8000/api/v1/titles/{titles_id}/ - получение информации о конкретном произведении ('GET')(Не аутентифицированный пользователь)  
http://127.0.0.1:8000/api/v1/titles/{titles_id}/ - частичное обновление информации о произведении ('PATCH')(Администратор или суперпользователь)  
http://127.0.0.1:8000/api/v1/titles/{titles_id}/ - удаление указанного произведения ('DELETE')(Администратор или суперпользователь)

http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/ - получение списка всех отзывов о произведении ('GET')(Не аутентифицированный пользователь), публикация нового отзыва ('POST')(Аутентифицированный пользователь)  
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/ - полуение конкретного отзыва по id ('GET')(Не аутентифицированный пользователь), частичное обновление отзыва по id ('PATCH')(Автор отзыва, модератор или администратор), удаление отзыва по id ('DELETE')(Автор отзыва, модератор или администратор)

http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/ - получение списка всех комментариев к отзыву ('GET')(Не аутентифицированный пользователь), публикация нового комментария ('POST')(Аутентифицированный пользователь)  
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ - полуение конкретного комментария к отзыву по id ('GET')(Не аутентифицированный пользователь), частичное обновление комментария по id ('PATCH')(Автор отзыва, модератор или администратор), удаление комментария по id ('DELETE')(Автор отзыва, модератор или администратор)

http://127.0.0.1:8000/api/v1/users/ - получение списка всех пользователей ('GET')(Администратор или суперпользователь), добавление нового пользователя ('POST')(Администратор или суперпользователь)   
http://127.0.0.1:8000/api/v1/users/{username}/ - получение конкретного пользователя по username ('GET')(Администратор или суперпользователь), изменение данных пользователя по username ('PATCH')(Администратор или суперпользователь), удаление пользователя по username ('DELETE')(Администратор или суперпользователь)     
http://127.0.0.1:8000/api/v1/users/me/ - получение данных своей учетной записи ('GET')(Аутентифицированный пользователь), изменение данных своей учетной записи ('PATCH')(Аутентифицированный пользователь)




### Разработчики проекта
- [Богомолов Игорь (тимлид, разработка ресурсов Auth и Users)](https://github.com/SpaiK89)
- [Молотков Виктор (разработка ресурсов Categories, Genres и Titles)](https://github.com/TwoSay95)
- [Супрун Александр (разработка ресурсов Review и Comments)](https://github.com/Aleksandr-SPb-Ru)