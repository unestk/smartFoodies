# SmartFoodies
🚀 This project is being developed together with Dominykas Bartauskas (https://github.com/DominykasBartauskas)

## Getting Started
### 1. Clone the repository
```
git clone https://github.com/DominykasBartauskas/smart_foodies.git
cd fastapi-backend
```
### 2. Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Set Up Environment Variables
```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
REDIS_URL=redis://localhost:6379
AUTH0_DOMAIN=your-auth0-domain
AUTH0_AUDIENCE=your-auth0-audience
SECRET_KEY=your-secret-key
ELASTICSEARCH_URL=http://localhost:9200
```
### 5. Run PostgreSQL, Redis, and Elasticsearch (Using Docker)
```
docker-compose up -d
```
### 6. Run Alembic Migrations (For Database Setup)
```
alembic upgrade head
```
### 7. Start the FastAPI Server
```
uvicorn app.main:app --reload
```
### 8. Start Celery Worker
```
celery -A app.worker.celery worker --loglevel=info
```
## Project Structure
```
project-root/
│-- app/
│   │-- main.py              # FastAPI entry point
│   │-- core/                # Core settings & configurations
│   │   │-- config.py        # Environment variables & settings
│   │   │-- database.py      # Database connection setup
│   │-- models/              # SQLAlchemy database models
│   │-- routers/             # API route handlers
│   │-- services/            # Business logic (Celery, Redis, Elasticsearch)
│-- migrations/              # Alembic migration files
│-- .env                     # Environment variables
│-- docker-compose.yml       # Docker setup
│-- Dockerfile               # Dockerfile for containerization
│-- requirements.txt         # Python dependencies
```
## Running in Docker
To run the full project in Docker, build and start the containers:
```
docker-compose up --build
```
This will set up:

- FastAPI Backend
- PostgreSQL Database
- Redis
- Elasticsearch
- Celery Worker
## Pre-Commit
### Installation
Make sure you have pre-commit installed:
```
pip install pre-commit
```
Then, install the pre-commit hooks:
```
pre-commit install
```
### Usage
Automatically runs when you commit code:
```
git commit -m "your message"
```
Run manually on all files:
```
pre-commit run --all-files
```
Skip pre-commit for a specific commit (not recommended):
```
git commit --no-verify -m "your message"
```
### Pre-commit Hooks Use
We use the following hooks (defined in .pre-commit-config.yaml):

- Black – Formats Python code to follow PEP 8
- Flake8 – Linting for code errors and style issues
- Trailing Whitespace Remover – Removes unnecessary spaces
- End-of-file Fixer – Ensures newline at the end of files
- Check YAML & JSON – Validates yaml and json files
## Authentication (Auth0)
This project uses Auth0 for authentication. To set up:

1. Create an Auth0 account.
2. Add the API Audience and Domain to your .env file.
3. Protect routes using FastAPI’s Depends(Auth0 dependency).
## Features
- FastAPI with JWT authentication
- PostgreSQL with Alembic migrations
- Redis for caching
- Celery for background tasks
- Elasticsearch integration
- Docker & Docker Compose for easy setup
## License
This project is licensed under the MIT License.
