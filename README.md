# 🎬 Cinema Booking System with Grok AI Integration

<div align="center">

![Cinema Booking](https://img.shields.io/badge/Cinema-Booking-red?style=for-the-badge&logo=movie)
![Grok AI](https://img.shields.io/badge/Grok-AI-blue?style=for-the-badge&logo=openai)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**An intelligent cinema ticket booking system powered by Large Language Models (LLMs), tool calling, and Gem AI for human-like interactions.**

*This project combines traditional APIs with conversational AI, enabling users to log in, chat naturally, and perform tasks like ticket booking, movie rescheduling, and payments through simple dialogue.*

[🚀 Quick Start](#-quick-start) • [📖 Documentation](#documentation) • [🔧 API Reference](#-api-endpoints) • [🤝 Contributing](#-contributing)


</div>

---


## 🌟 Key Features

> “This system allows users to interact naturally with AI to book, reschedule, and pay — no manual form filling required.”


- **🔑 User Authentication** – Secure login & signup system
- **💬 Conversational Booking** – Interact with an LLM chatbot (Grok / LLaMA2)
- **🛠 Tool Calling** – Backend functions for:
  - Movie ticket booking
  - Rescheduling
  - Payments
  - Greetings & other utilities
- **🧠 Gen AI Integration** – Humanizes LLM outputs, making them more natural and engaging
- **🧪 API Testing with Postman** – Pre-configured collection for testing endpoints
---

## 🛠 Technologies

Python | FastAPI | SQLite | Postman | LLMs (Grok, LLaMA2) | JSON | Gen AI 

---
<a id="documentation"></a>
## 🏗️ System Architecture

```mermaid
flowchart TD
    A[User Login] --> B[LLM - Grok / LLaMA2]
    B -->|Tool Call| C[FastAPI Backend]
    C -->|book_ticket, reschedule_ticket, payment| D[Database]
    C --> E[Return JSON Response]
    E --> F[Gem AI Humanizer]
    F --> G[Final Human-like Reply]
```

## 🚀 Quick Start

### Prerequisites

```bash
Python >= 3.8
FastAPI
Postman (for API testing)
API Keys: Grok, LLaMA2, Gem AI
Database: SQLite
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mirza-Muhammed/cinema-booking-grok.git
   cd cinema-booking-grok
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configurations
   ```

5. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

## 📁 Project Structure

```
cinema-booking-grok/
├── 📂 app/
│   ├── 📂 auth/               # Authentication modules
│   ├── 📂 llm/                # LLM integration (Grok, LLaMA2)
│   ├── 📂 tools/              # Tool calling functions
│   ├── 📂 models/             # Database models
│   ├── 📂 api/                # API routes
│   └── 📂 utils/              # Helper functions
├── 📂 postman/                # Postman collections
├── 📂 tests/                  # Test files
├── 📄 main.py                 # FastAPI application entry point
├── 📄 requirements.txt        # Python dependencies
├── 📄 .env.example           # Environment variables template
└── 📄 README.md              # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Database Configuration
DATABASE_URL=sqlite:///./cinema_booking.db

# Authentication
JWT_SECRET_KEY=your_super_secret_jwt_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# LLM APIs
GROK_API_KEY=your_grok_api_key
GROK_API_URL=https://api.x.ai/v1/chat/completions
LLAMA_API_KEY=your_llama_api_key
LLAMA_API_URL=http://localhost:8000

# Gem AI
GEM_AI_API_KEY=your_gem_ai_key
GEM_AI_PERSONALITY=friendly_cinema_assistant

# External Services
PAYMENT_GATEWAY_KEY=your_payment_gateway_key
CINEMA_API_KEY=your_cinema_api_key

# Server Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=True
```

## 🔌 API Endpoints

> **Note:** All POST endpoints accept JSON payloads as request body.
### Authentication

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `POST` | `/auth/signup` | Register new user | `{"username": "string", "email": "string", "password": "string"}` |
| `POST` | `/auth/login` | User login | `{"username": "string", "password": "string"}` |
| `GET` | `/auth/me` | Get current user | Header: `Authorization: Bearer <token>` |

### LLM Chat Interface

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `POST` | `/chat` | Send message to AI | `{"message": "string", "model": "grok/llama2"}` |
| `GET` | `/chat/models` | Get available models | - |
| `POST` | `/chat/switch-model` | Switch LLM model | `{"model": "grok/llama2"}` |

### Tool Calling Functions

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `POST` | `/tools/book-ticket` | Book movie tickets | `{"movie_id": "string", "theater_id": "string", "showtime": "datetime", "seats": ["string"]}` |
| `POST` | `/tools/reschedule-ticket` | Reschedule booking | `{"booking_id": "string", "new_showtime": "datetime"}` |
| `POST` | `/tools/process-payment` | Process payment | `{"booking_id": "string", "amount": "float", "method": "string"}` |
| `GET` | `/tools/available` | Get available tools | - |

### Movie & Theater Data

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/movies` | Get all movies |
| `GET` | `/theaters` | Get all theaters |
| `GET` | `/showtimes/{movie_id}` | Get showtimes for movie |

## 📝 Example Usage

### 1. User Authentication
```bash
# Register
curl -X POST "http://localhost:8000/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "email": "john@example.com", "password": "secure123"}'

# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "password": "secure123"}'
```

### 2. Chat with AI
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  -d '{"message": "I want to book tickets for Avengers this Friday evening", "model": "grok"}'
```

### 3. Direct Tool Calling
```bash
# Book ticket
curl -X POST "http://localhost:8000/tools/book-ticket" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  -d '{
    "movie_id": "movie_123",
    "theater_id": "theater_456",
    "showtime": "2024-01-15T19:30:00",
    "seats": ["A12", "A13"]
  }'
```

## 🧪 Testing with Postman

1. **Import Collection**
   - Import the collection from `/postman/Cinema-Booking-Grok.postman_collection.json`
   - Import environment from `/postman/Cinema-Booking-Environment.postman_environment.json`

2. **Authentication Flow**
   - Run the `Signup` request
   - Run the `Login` request (token will be auto-stored)
   - All subsequent requests will use the token automatically

3. **Test Chat Interface**
   - Use the `Chat with AI` request
   - Try different models: Grok vs LLaMA2
   - Test various booking scenarios

## 🤖 LLM Integration Details

### Available Models

| Model | Strengths | Best For |
|-------|-----------|----------|
| **Grok** | Advanced reasoning, context understanding | Complex queries, recommendations |
| **LLaMA2** | Fast responses, reliable tool execution | General chat, quick bookings |

### Tool Calling Schema

```python
# Example tool definition
tools = [
    {
        "name": "book_ticket",
        "description": "Books movie tickets for the user",
        "parameters": {
            "type": "object",
            "properties": {
                "movie_id": {"type": "string", "description": "Movie ID"},
                "theater_id": {"type": "string", "description": "Theater ID"},
                "showtime": {"type": "string", "description": "Showtime in ISO format"},
                "seats": {"type": "array", "items": {"type": "string"}}
            },
            "required": ["movie_id", "theater_id", "showtime", "seats"]
        }
    }
]
```

### Gem AI Humanization

```python
async def humanize_response(llm_response: str, context: str) -> str:
    """Humanize LLM response using Gem AI"""
    response = await gem_ai_client.humanize(
        text=llm_response,
        context=context,
        personality="friendly_cinema_assistant"
    )
    return response.humanized_text
```

## 📊 Response Examples

### Chat Response with Tool Calling
```json
{
  "status": "success",
  "message": "Perfect! I've found some great action movies for Friday evening. 'Avengers: Endgame' is playing at 7:30 PM at PVR Cinemas. Would you like me to book 2 tickets for you?",
  "model_used": "grok",
  "tools_called": ["search_movies", "get_showtimes"],
  "humanized": true,
  "suggested_actions": [
    {
      "action": "book_ticket",
      "movie": "Avengers: Endgame",
      "theater": "PVR Cinemas",
      "showtime": "2024-01-15T19:30:00"
    }
  ]
}
```

### Successful Booking
```json
{
  "status": "success",
  "message": "Awesome! I've successfully booked 2 tickets for 'Avengers: Endgame' at PVR Cinemas for Friday, 7:30 PM. Your seats are A12 and A13. Total amount: ₹500. You'll receive a confirmation email shortly!",
  "data": {
    "booking_id": "BK123456",
    "movie": "Avengers: Endgame",
    "theater": "PVR Cinemas",
    "showtime": "2024-01-15T19:30:00Z",
    "seats": ["A12", "A13"],
    "total_amount": 500,
    "payment_status": "completed"
  }
}
```

## 🛠️ Development

### Running in Development Mode
```bash
# With auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# With debug logging
uvicorn main:app --reload --log-level debug
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_auth.py -v
```

### Code Quality
```bash
# Format code
black app/
isort app/

# Lint code
flake8 app/
mypy app/
```

## 🐳 Docker Support

```dockerfile
# Dockerfile example
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build and run
docker build -t cinema-booking-grok .
docker run -p 8000:8000 --env-file .env cinema-booking-grok
```

## 🚀 Deployment

### Production Setup
```bash
# Install production dependencies
pip install gunicorn

# Run with Gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Environment Variables for Production
```env
DEBUG=False
DATABASE_URL=postgresql://user:password@localhost:5432/cinema_booking
REDIS_URL=redis://localhost:6379/0
```

## 📈 Performance & Monitoring

- **Caching**: Redis for session and response caching
- **Database**: PostgreSQL for production, SQLite for development
- **Monitoring**: Built-in FastAPI metrics at `/metrics`
- **Logging**: Structured logging with correlation IDs

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Write tests for new features
- Update documentation
- Use type hints
- Add docstrings to functions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Grok AI** for advanced language understanding
- **LLaMA2** for efficient text generation
- **Gem AI** for response humanization
- **FastAPI** for the robust web framework

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Mirza-Muhammed/cinema-booking-grok/issues)
- **Email**: mirzamuhammedofficial@gmail.com
- **Documentation**: [Project Wiki](https://github.com/Mirza-Muhammed/cinema-booking-grok/wiki)

---

<div align="center">

**Made with ❤️ by [Mirza Muhammed](https://github.com/Mirza-Muhammed)**

⭐ Star this repository if you found it helpful!

</div>
