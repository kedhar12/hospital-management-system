# Deployment Notes

This document describes how to deploy the Hospital Management System to Render (or similar PaaS) and how to run locally.

## Render (Python web service)

1. **Create a new Web Service** on Render using this Git repository.
2. **Build command**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Start command**:

    ```bash
    gunicorn hospital_project.wsgi:application --bind 0.0.0.0:$PORT
    ```

4. **Environment variables** to add on Render (Settings → Environment):
   - `SECRET_KEY` — a secure random string (generate with `django.core.management.utils.get_random_secret_key()`)
   - `DJANGO_DEBUG` — set to `False`
   - `DATABASE_URL` — from the Postgres add-on
   - `REDIS_URL` — from the Redis add-on
   - `CELERY_BROKER_URL` and `CELERY_RESULT_BACKEND` — can point to the same `REDIS_URL`
   - Any other production-specific vars such as `EMAIL_HOST`, `ALLOWED_HOSTS`, etc.

5. **Attach services**:
   - Add a managed **Postgres** database and copy its URL into `DATABASE_URL`.
   - Add a **Redis** instance and copy its URL to `REDIS_URL` (and Celery vars).

6. **Static files**:
   - Render runs `collectstatic` automatically if `DJANGO_SETTINGS_MODULE` is set. Otherwise, add a **Release Command**:
     ```bash
     python manage.py collectstatic --noinput
     ```
   - Ensure `STATIC_ROOT` is set in `settings.py` (already configured).

7. **Manual migrations**:
   - After deployment, run `python manage.py migrate` in the Shell tab or via a deploy hook.

---

### Optional: Deploying to Heroku (Alternatives)

1. Create a new Heroku app.
2. Add the **Heroku Postgres** and **Heroku Redis** add-ons.
3. In the Heroku Dashboard > Settings, set the same environment variables as above.
4. Add a `Procfile` to the repo:

    ```Procfile
    web: gunicorn hospital_project.wsgi
    ```

5. Push to Heroku using Git:

    ```bash
    git push heroku main
    heroku run python manage.py migrate
    heroku run python manage.py collectstatic --noinput
    ```

6. Set `DEBUG=False` and configure `ALLOWED_HOSTS` to the Heroku app URL.

---

### Deploy Checklist

- [ ] `SECRET_KEY` not checked into repo
- [ ] `DJANGO_DEBUG=False`
- [ ] External services (DB/Redis) added
- [ ] Migrations applied
- [ ] Static files collected
- [ ] Admin superuser created
- [ ] `ALLOWED_HOSTS` configured

---

## Running Locally (development)

1. Create virtual environment and install requirements:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Run migrations and create a superuser:

```bash
py manage.py migrate
py manage.py createsuperuser
```

3. Start the dev server:

```bash
py manage.py runserver
```

4. To run Celery worker locally (requires Redis running):

```bash
celery -A hospital_project worker -l info
```

---

## Notes

- Ensure `DEBUG=False` in production.
- Use strong `SECRET_KEY` and secure DB credentials.
- Configure email and other production settings as needed.
- Monitor logs and set up error reporting (Sentry, etc.).

## Running Locally (development)

1. Create virtual environment and install requirements:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Run migrations and create a superuser:

```bash
py manage.py migrate
py manage.py createsuperuser
```

3. Run dev server:

```bash
py manage.py runserver
```

4. To run Celery worker locally (requires Redis running):

```bash
celery -A hospital_project worker -l info
```

## Notes
- Ensure `DEBUG=False` in production.
- Use strong `SECRET_KEY` and secure DB credentials.
- Configure email and other production settings as needed.
