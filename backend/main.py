"""
Мини-анкета — Backend (FastAPI)
GET  /questions — список вопросов
POST /answers   — приём и сохранение ответов в памяти
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Mini Survey API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Вопросы (жёстко заданные) ────────────────────────────────────────────────

QUESTIONS = [
    {"id": 1, "text": "Как вас зовут?", "type": "text"},
    {"id": 2, "text": "Сколько вам лет?", "type": "number"},
    {"id": 3, "text": "Какой ваш любимый язык программирования?", "type": "choice",
     "options": ["Python", "JavaScript", "Go", "TypeScript", "Другой"]},
    {"id": 4, "text": "Оцените ваш опыт программирования от 1 до 10", "type": "number"},
    {"id": 5, "text": "Что бы вы хотели изучить в ближайшее время?", "type": "text"},
]

# ── Хранилище ответов (in-memory) ────────────────────────────────────────────

answers_store: list[dict] = []

# ── Модели ────────────────────────────────────────────────────────────────────

class AnswerItem(BaseModel):
    question_id: int
    answer: str

class AnswersPayload(BaseModel):
    answers: list[AnswerItem]

# ── Эндпоинты ────────────────────────────────────────────────────────────────

@app.get("/questions")
def get_questions():
    return {"questions": QUESTIONS}


@app.post("/answers")
def post_answers(payload: AnswersPayload):
    entry = {a.question_id: a.answer for a in payload.answers}
    answers_store.append(entry)
    return {"status": "ok", "total_responses": len(answers_store)}


@app.get("/answers")
def get_all_answers():
    """Вспомогательный эндпоинт — посмотреть все сохранённые ответы."""
    return {"responses": answers_store, "total": len(answers_store)}
