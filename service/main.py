from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# экземпляр FastAPI
app = FastAPI()


# модель для входящего JSON
class QuestionRequest(BaseModel):
    questions_num: int


# модель для таблицы в базе данных
Base = declarative_base()


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String)
    answer_text = Column(String)
    created_at = Column(DateTime, server_default=text("NOW()"))


# подключение к PostgreSQL
DATABASE_URL = os.getenv("DB_URL")
engine = create_engine(DATABASE_URL)

# создание таблицы, если она не существует
Base.metadata.create_all(bind=engine)

# создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# эндпоинт для получения вопросов и сохранения их в базу данных
@app.post("/get_questions/")
async def get_questions(request_data: QuestionRequest):
    session = SessionLocal()
    last_question = session.query(Question).order_by(Question.id.desc()).first()
    try:
        while True:
            response = requests.get(f"https://jservice.io/api/random?count={request_data.questions_num}")
            questions_data = response.json()
            for question_data in questions_data:
                question = Question(
                    question_text=question_data['question'],
                    answer_text=question_data['answer'],
                )
                existing_question = session.query(Question).filter_by(question_text=question.question_text).first()
                if not existing_question:
                    session.add(question)
                    session.commit()
            if last_question:
                return {
                    "id": last_question.id,
                    "question_text": last_question.question_text,
                    "answer_text": last_question.answer_text,
                    "created_at": last_question.created_at
                }
            else:
                return {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()
