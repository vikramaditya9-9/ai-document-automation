# DocuFlow AI — Document Automation Platform

An AI-powered platform that automatically classifies documents, extracts structured information, validates business data, and routes documents through configurable approval workflows with human-in-the-loop review.

## 🎯 Overview

DocuFlow AI automates document processing workflows, starting with invoice processing. The platform:

- **Classifies** incoming documents using AI
- **Extracts** structured data (vendor name, amounts, dates, etc.)
- **Validates** extracted information against business rules
- **Routes** documents for automatic approval or human review
- **Provides** audit trails and workflow history
- **Supports** role-based access control (User, Reviewer, Admin)

## 📋 Current Phase

**Phase 1: Project Foundation** ✅
- FastAPI application structure
- Configuration management
- Health check endpoint
- Environment variable setup

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### 1. Clone the Repository

```bash
git clone https://github.com/vikramaditya9-9/ai-document-automation.git
cd ai-document-automation
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env if needed (defaults are suitable for local development)
```

### 5. Run the Application

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The application will start at: **http://localhost:8000**

## 📚 Available Endpoints

### Interactive API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint with API info |
| GET | `/health` | Health check endpoint |

## 🏗️ Project Structure

```
ai-document-automation/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py           # Configuration management
│   ├── api/                    # API route handlers (Phase 2+)
│   ├── models/                 # Database models (Phase 2+)
│   ├── schemas/                # Request/response schemas (Phase 2+)
│   ├── services/               # Business logic (Phase 2+)
│   ├── database/               # Database setup (Phase 2+)
│   └── tests/                  # Unit and integration tests
├── requirements.txt            # Project dependencies
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
└── LICENSE                     # Project license
```

## 🔧 Configuration

The application uses environment variables for configuration. See `.env.example` for all available settings:

- `DATABASE_URL` - Database connection string
- `JWT_SECRET_KEY` - Secret key for JWT tokens
- `AI_PROVIDER` - AI provider (mock, openai, etc.)
- `MAX_UPLOAD_SIZE_MB` - Maximum file upload size
- `DEBUG` - Enable debug mode

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| fastapi | 0.104.1 | Web framework |
| uvicorn | 0.24.0 | ASGI server |
| pydantic | 2.5.0 | Data validation |
| pydantic-settings | 2.1.0 | Settings management |
| python-dotenv | 1.0.0 | Environment variables |
| sqlalchemy | 2.0.23 | ORM (for Phase 2+) |

## 📍 Development Roadmap

### Phase 1: Foundation ✅
- [x] Project structure
- [x] FastAPI setup
- [x] Health check
- [x] Configuration

### Phase 2: Database
- [ ] PostgreSQL setup
- [ ] User model
- [ ] Database migrations

### Phase 3: Authentication
- [ ] User registration
- [ ] Login/JWT
- [ ] Role-based access control

### Phase 4: Document Management
- [ ] File upload handling
- [ ] Document storage
- [ ] Document listing

### Phase 5-10: Advanced Features
- [ ] Invoice processing
- [ ] AI extraction
- [ ] Validation engine
- [ ] Workflow routing
- [ ] Frontend UI
- [ ] Testing & deployment

## 🧪 Testing

Tests will be added in Phase 10. Currently, you can verify the application:

```bash
# Test the health endpoint
curl http://localhost:8000/health

# Visit the interactive documentation
# Open http://localhost:8000/docs in your browser
```

## 🔐 Security

- ✅ Environment variables for secrets (never commit `.env`)
- ✅ JWT token support ready for Phase 3
- ⚠️ Database encryption - Phase 2+
- ⚠️ File validation - Phase 4+

## 📝 License

See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

This project follows the AI 4D Development Framework from the master specification in `.prompts/document.md`:
- **D1 — Delegation**: Coordinated team roles
- **D2 — Description**: Clear business requirements
- **D3 — Discernment**: Smart technical decisions
- **D4 — Diligence**: Execution standards

## 📞 Support

For detailed architecture and development guidelines, see `.prompts/document.md`
