# Shorty Link

Shorty Link is a URL shortener designed to turn long links into short, easy-to-share URLs. The project combines a backend with user authentication and a modern frontend to manage links, create quick access shortcuts, and maintain a user dashboard.

## Short description

The application allows:

- Registering and logging in users.
- Creating, listing, editing, and deleting shortened URLs.
- Generating short codes that redirect to the original URL.
- Managing sessions and JWT tokens.
- Accessing a web interface built with Vue to view and manage links.

## Tech stack

### Backend
- Python 3.12
- Django 6.1
- Django Ninja 1.7.0
- PostgreSQL
- JWT for authentication
- CORS and WhiteNoise
- Granian as the WSGI server

The backend dependencies are defined in [backend/requirements.txt](backend/requirements.txt).

### Frontend
- Vue 3
- Vite
- TypeScript
- Vue Router
- Tailwind CSS
- ESLint + Vitest

The frontend configuration is defined in [frontend/package.json](frontend/package.json).

### Infrastructure
- Docker
- Docker Compose

## Project structure

- [backend/](backend/) — API, models, authentication, services, migrations, and tests.
- [frontend/](frontend/) — Vue application with routes, services, and components.
- [docker-compose.yaml](docker-compose.yaml) — starts the backend and database.
- [bruno/](bruno/) — API request collection for testing.

## Requirements

Before running the project, make sure you have installed:

- Docker and Docker Compose
- Node.js 22.18+ or 24.12+
- npm
- Python 3.12
- PostgreSQL (if you want to run the database locally without Docker)

## Environment variables

The backend uses environment variables for Django, database, and JWT configuration. You can create a `.env` file inside `backend/` with values similar to the following:

```env
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
HOSTS=localhost,127.0.0.1
DB_NAME=shorty_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
JWT_SECRET_KEY=your-jwt-secret
ALGORITHM=HS256
ACCESS_TTL=15
REFRESH_TTL=7
CORS_ALLOWED_ORIGINS=http://localhost:5173
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
```

## How to run the project

### Option 1: with Docker (recommended)

From the project root:

```bash
docker compose up --build
```

This will start:

- Backend at: http://localhost:8000
- PostgreSQL database in the `db` container

### Option 2: backend locally

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### Option 3: frontend locally

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at:

- http://localhost:5173

## Useful commands

### Frontend

```bash
cd frontend
npm run build
npm run test:unit
npm run lint
```

### Backend

```bash
cd backend
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

## Additional notes

- The backend uses `django-ninja` to build the API.
- The project includes a Bruno API test collection in [bruno/](bruno/).
- The frontend is built with Vue and Vite, while the backend is built with Django, so development can proceed independently in each part.

## License

This project is distributed under the license included in [LICENSE](LICENSE).
