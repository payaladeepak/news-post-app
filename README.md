# 📰 News Post App

## Overview
News Post App is a modern **content publishing platform** (mobile-first, bilingual: English + Hindi) with:
- FastAPI backend (REST/GraphQL ready)
- Next.js frontend (cards, sliders, swipe animations, mobile-first UI)
- Postgres + Redis + MinIO (object storage)
- CI/CD via GitHub Actions
- Docker Compose based local + server environment

---

## 🏗️ Current Setup (as of Oct 2, 2025)

### Repository
- GitHub: [payaladeepak/news-post-app](https://github.com/payaladeepak/news-post-app)
- Branch: `main`

### Backend (FastAPI)
- Base project scaffold created
- Models:
  - `User` (auth, roles, timestamps)
  - `Post` (title, slug, body, views, status)
- Alembic migrations initialized & applied ✅
- Database: **newsdb**
- Endpoint: `/health` → returns `{"status":"ok"}`

### Frontend (Next.js 14)
- Scaffold created with placeholder page
- Dev server runs on port **3000**
- CI workflow builds frontend via `npm run build`

### Infrastructure
- Docker Compose stack (`infra/docker-compose.yml`):
  - Postgres @ `5432`
  - Redis @ host `6380` (mapped to 6379 inside)
  - MinIO @ `9000, 9001`
  - API @ host `8001`
  - Frontend @ host `3000`
- All containers running fine (`docker compose ps` verified)

### CI/CD
- GitHub Actions added:  
  - Frontend build check  
  - Backend sanity check (Python 3.10, sqlalchemy, alembic)

---

## 🛠️ Local Development

```bash
# Start stack (from project root)
docker compose -f infra/docker-compose.yml up --build -d

# Check logs
docker compose -f infra/docker-compose.yml logs -f api frontend

# Health check
curl http://localhost:8001/health

