# EVA4 – Reservas / Ramos (Django)

> **Proyecto académico** (Evaluación 4, dic-2024). Antecesor de [EduPredict](https://github.com/nelsonpt-sys/EduPredict).

Aplicación web en Django para gestionar reservas y ramos con control de estados.

## Stack
Django, MySQL (base `DJANGO_RESERVAS2`), HTML/CSS.

## Ejecución local
```bash
python -m venv .venv && source .venv/bin/activate
pip install django mysqlclient
# Crea la base MySQL DJANGO_RESERVAS2 y ajusta usuario/clave en EVA4_FINAL/settings.py
python manage.py migrate
python manage.py runserver
```
`SECRET_KEY` se lee de la variable de entorno del mismo nombre (hay un valor de desarrollo por defecto).
