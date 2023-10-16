# bewise_testcase

в текущей директории проекта выполните следующую команду
# docker-compose up --build

# после этой команды контейнеры сами соберутся и запустятся

пример запроса к серверу

# curl -X POST "http://localhost:8000/get_questions/" -H "Content-Type: application/json" -d '{"questions_num": 3}'
