# ОБРАЗ FASTAPI ОФИЦИАЛЬНЫЙ 
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# РАБОЧАЯ ПАПКА ВНУТРИ КОНТЕЙНЕРА
WORKDIR /app

# КОПИРОВАТЬ СОДЕРЖИМОЕ ПРОЕКТА В ПАПКУ app
COPY service /app

# загрузить все зависимости 
RUN pip install -r /app/requirements.txt

# порт 80 чтобы можно было обращаться к машине
EXPOSE 80

# запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


