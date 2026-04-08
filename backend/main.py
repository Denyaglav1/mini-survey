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
    {"id": 1, "text": "Как к вам обращаться в pull-request'ах?", "type": "text"},
    {"id": 2, "text": "Сколько вам лет?", "type": "number"},
    {"id": 3, "text": "Какой у вас любимый AI-помощник для вайбкодинга?", "type": "choice",
     "options": ["ChatGPT", "Claude", "Copilot", "Cursor", "v0 by Vercel",
                 "Я и есть AI, просто никто не знает"]},
    {"id": 4, "text": "Что вы делаете, когда AI сгенерировал 500 строк кода?", "type": "choice",
     "options": ["Копирую не глядя — вайб же!", "Делаю вид, что читаю",
                 "Прошу объяснить, потом всё равно копирую",
                 "Удаляю и прошу заново, но вежливее",
                 "Плачу в Figma"]},
    {"id": 5, "text": "Сколько раз в день вы говорите «это же просто кнопка, почему так сложно»?",
     "type": "choice",
     "options": ["0 — я уже смирился", "1–3 раза", "4–10 раз",
                 "Это мой внутренний монолог 24/7",
                 "Я автоматизировал эту фразу через макрос"]},
    {"id": 6, "text": "Сколько лет вы уже программируете?", "type": "number"},
    {"id": 7, "text": "Ваш уровень вайбкодинга (1 — «что такое терминал», 10 — «деплою взглядом»)",
     "type": "number"},
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
