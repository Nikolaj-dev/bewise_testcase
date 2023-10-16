# bewise_testcase

Этот README-файл содержит информацию о том, как запустить проект, как выполнять запросы к серверу и как инициализировать базу данных. 

Пример Docker-проекта, который включает в себя FastAPI-приложение и PostgreSQL в контейнерах Docker. Проект позволяет выполнять запросы к FastAPI-серверу для получения вопросов для викторины.

## Запуск проекта

Скачайте данный репозиторий как zip-архив или при помощи команды - git clone

Для запуска проекта выполните следующие шаги:

1. В корневой директории проекта выполните следующую команду, чтобы собрать и запустить контейнеры:
   ```bash
   docker-compose up --build

Контейнеры сами соберутся и запустятся.

## Пример запроса к серверу

Ubuntu/Debian(обязательно порт 80):

Запускаем прямо из терминала приложения в котором находится fastapi

curl -X POST "http://localhost:80/get_questions/" -H "Content-Type: application/json" -d '{"questions_num": 3}'

Windows на примере программы Postman(обязательно порт 8000):

http://localhost:8000/get_questions/

Метод: POST

В пункте body выбрать тип raw/json

{"questions_num": 1}

