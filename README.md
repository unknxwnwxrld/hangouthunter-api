# 🔍 HangoutHunter API

**Intelligent backend for discovering atmospheric venues**  
A FastAPI service that understands natural language queries in Russian (and English), using Google Gemini to recommend 10–20 real restaurants, cafes, bars, and other spots — focusing on unique, high-rated places while avoiding tourist traps and large chains.

Perfect as a backend for a Telegram bot (@HangoutHunterBot or similar).

### ✨ Features
- 🧠 Natural language query processing powered by Google Gemini  
- 🌍 Support for any location  
- 🌐 Responses in any langiage
- 🎯 Emphasis on unique concepts, great atmosphere, and high-quality experiences  
- 🚫 Strict prompt engineering to recommend only real, existing venues  
- 📊 Request and response validation with Pydantic  

### 🚀 Quick Start

```bash
git clone https://github.com/unknxwnwxrld/hangouthunter-api.git
cd hangouthunter-api

cp .env.example .env  # ← add your GEMINI_API_KEY

pip install -r requirements.txt

uvicorn app.main:app --reload
```
The API will be available at: http://127.0.0.1:8000<br>
Interactive docs: http://127.0.0.1:8000/docs (Swagger UI) • http://127.0.0.1:8000/redoc

### 📸 Usage Examples
#### Request
```bash
curl -X POST http://127.0.0.1:8000/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "city": "Moscow",
    "criteria": "cozy cafe with vegetarian menu and great coffee in the city center",
    "lang": "english"
  }'
```

#### Response (excerpt)
```json
{
  "venues": [
    {
      "name": "Coffee and Books",
      "cuisine": "vegetarian, coffee & desserts",
      "why_visit": "A cozy spot with bookshelves, live plants, and signature egg-free, milk-free desserts.",
      "address_hint": "Tverskaya Street, near Mayakovskaya metro"
    },
    ...
  ]
}
```
### 🛠 Tech Stack
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green)
![Google Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-orange)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-lightgrey)

### 🤖 Live Telegram Bot
This API directly powers the live Telegram bot [@HangoutHunterBot](https://t.me/HangoutHunterBot), where users can discover unique and atmospheric venues using simple natural language queries right in the chat.<br>
The full source code for the bot is available here: [hangouthunter-telegram-bot](https://github.com/unknxwnwxrld/hangouthunter-telegram-bot).

### 🔜 Roadmap
- Docker + docker-compose support
- Response caching (Redis)
- Rate limiting and abuse protection
- Integration with Google Places / 2GIS API for photos and up-to-date links
- Tests and CI/CD pipeline

### 🤝 Contributing
Contributions are welcome! Feel free to open issues and pull requests.

### 📄 License
MIT © unknxwnwxrld<br>
⭐ If you find this project useful — give it a star!
