# CandidateValidate

CandidateValidate is a web application designed to empower voters by providing them with instant access to their political candidates' backgrounds, specifically focusing on criminal records and declared assets. 

This project consists of a Next.js (App Router) frontend and a Python FastAPI backend connected to a PostGIS-enabled PostgreSQL database.

## Architecture & Tech Stack

- **Frontend**: Next.js 16 (React 19), Tailwind CSS, MapLibre GL JS, Recharts, Lucide React.
- **Backend**: Python 3, FastAPI, SQLAlchemy (Core).
- **Database**: PostgreSQL with PostGIS extension.
- **AI Integration**: Google Generative AI (Gemini Pro) for intuitive candidate profile analysis.

## Local Development Setup

> **Note**: These instructions assume you already have the `cv_postgres_db` docker container running with the application's database.

### 1. Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure Environment Variables:
   - Copy `backend/.env.example` to `backend/.env`
   - Add your Gemini API key to `GEMINI_API_KEY`
   - Your `DATABASE_URL` will default to `postgresql://postgres:password@localhost:5432/cvdb` if not set, which matches your local Docker setup.
5. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### 2. Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Configure Environment Variables:
   - Copy `frontend/.env.example` to `frontend/.env.local`
   - By default, it points to `http://127.0.0.1:8000` for local development.
4. Start the development server:
   ```bash
   npm run dev
   ```

## Deployment Instructions

### Database Export (From Docker)
To deploy the database to a live server (like Render PostgreSQL), you must first export your local database from your running Docker container.

Run this command from your terminal:
```bash
docker exec -t cv_postgres_db pg_dump -U postgres -d cvdb -F c -f /tmp/cvdb.dump
docker cp cv_postgres_db:/tmp/cvdb.dump ./cvdb.dump
```
*(This creates a binary dump file named `cvdb.dump` in your current directory. It is ignored by Git due to its size).*

You can then use `pg_restore` to push this dump to your managed database provider (e.g. Render).

### Frontend Deployment (Vercel)
1. Push this repository to GitHub.
2. Sign in to [Vercel](https://vercel.com/) and create a new project.
3. Connect your GitHub repository.
4. Set the **Framework Preset** to `Next.js`.
5. Set the **Root Directory** to `frontend`.
6. Add the Environment Variable `NEXT_PUBLIC_API_URL` pointing to your deployed backend URL.
7. Click **Deploy**.

### Backend Deployment (Render)
1. Sign in to [Render](https://render.com/) and create a new **Web Service**.
2. Connect your GitHub repository.
3. Set the **Root Directory** to `backend`.
4. Set the **Environment** to `Python 3`.
5. Set the **Build Command** to `pip install -r requirements.txt`.
6. Set the **Start Command** to `uvicorn main:app --host 0.0.0.0 --port $PORT`.
7. Add Environment Variables:
   - `DATABASE_URL`: Add your remote Render PostgreSQL connection string.
   - `GEMINI_API_KEY`: Add your Gemini API key.
8. Click **Create Web Service**.
