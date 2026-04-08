# Мини-анкета

Full-stack приложение: backend (FastAPI) + frontend (HTML/JS).

## Функционал

- `GET /questions` — возвращает список вопросов анкеты (5 шт.)
- `POST /answers` — принимает ответы пользователя, сохраняет в памяти
- `GET /answers` — просмотр всех сохранённых ответов (вспомогательный)
- Frontend загружает вопросы, отображает форму, отправляет ответы и показывает «Спасибо!»

## Запуск

### 1. Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Backend будет доступен на `http://localhost:8000`

### 2. Frontend

Просто откройте файл `frontend/index.html` в браузере.

Или через любой HTTP-сервер:
```bash
cd frontend
python -m http.server 3000
```
Затем откройте `http://localhost:3000`

## Технологии

- **Backend**: Python 3.12+, FastAPI, Uvicorn
- **Frontend**: HTML, CSS, JavaScript (без фреймворков)
- **Хранение данных**: in-memory (list в Python)

## Структура проекта

```
mini-survey/
├── backend/
│   ├── main.py              # FastAPI приложение
│   └── requirements.txt     # Зависимости Python
├── frontend/
│   └── index.html           # Интерфейс анкеты
├── prompts.md               # Использованные промпты
├── screenshots/             # Скриншоты работы
├── .gitignore
└── README.md
```

## Использованные промпты

См. файл [prompts.md](prompts.md)
