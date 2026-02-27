# Hospital Management System

This repository contains a Django + DRF backend with JWT, PostgreSQL, Redis caching, Gunicorn, Whitenoise and Docker setup.

Features:
- JWT Authentication (Simple JWT)
- Role-based access: Admin, Doctor, Patient
- Models: Doctor, Patient, Appointment, Prescription, Invoice
- Redis caching for dashboard
- Docker + docker-compose (Postgres + Redis)

Quick start (development):

1. Copy `.env.example` to `.env` and set values.
2. Build and start:

```bash
docker compose up --build
```

API endpoints under `/api/`.

Local quick start (without Docker):

```bash
py -m venv .venv
source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows
pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Deployment: See `DEPLOYMENT.md` for Render and production notes.
