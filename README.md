# 🍴 HangoutHunter API – Smart backend for finding establishments

A FastAPI service that acts as a backend for a Telegram bot that searches for restaurants, cafes, bars, street food, and other catering establishments.

### Key features
- Accepts natural user queries in English, Russian or Ukrainian languages (for example: “Where can I eat sushi in the city center without spending a lot?” or “A cool bar with live music near the metro station”).
- Processing requests using **Google Gemini** (a neural network analyzes the intent and extracts parameters: type of establishment, cuisine, budget, area, atmosphere, etc.).
- Return a structured list of suitable establishments with photos, ratings, addresses, links, and a brief justification for the selection.
- Ready-made API for easy connection to a Telegram bot (webhook or polling).

### Technologies
- **FastAPI** — a fast and modern framework
- **Google Gemini API** — powerful natural language processing
- **Pydantic** — data validation and serialization
- **Uvicorn** — ASGI server
- Docker support (in development)

### Why this project?
The bot understands requests as if it were communicating with a real person, rather than forcing you to choose from rigid filters. Ideal for those who are tired of template-based search engines for establishments.

### Installation and launch
```bash
git clone https://github.com/yourusername/foodspot-api.git
cd foodspot-api
cp .env.example .env  # fill in GEMINI_API_KEY and other variables
pip install -r requirements.txt
uvicorn app.main:app --reload
