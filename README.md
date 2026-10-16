# Ojo Ciudadano

Sistema de reportes ciudadanos para Pereira, Risaralda: los ciudadanos
reportan problemas (seguridad, aseo, ruido, espacio público, etc.)
con evidencia fotográfica/de video y ubicación, y cada reporte se
dirige a la entidad competente.

## Estado del proyecto

Se construye por etapas (ver `docs/ARCHITECTURE.md` cuando exista, y
el documento de especificación original del proyecto). Hoy está
completa la:

- **Etapa 1 — Backend y base de datos:** estructura del repositorio,
  Django + Django REST Framework, PostgreSQL con PostGIS, modelo de
  usuario inicial, endpoint de verificación (`/api/v1/health/`) y
  pruebas automatizadas básicas.

Pendientes: autenticación y roles (Etapa 2), API de reportes (Etapa
3), app móvil (Etapa 4), geolocalización y evidencias (Etapa 5),
panel administrativo (Etapa 6), y las siguientes.

## Estructura

```
apps/mobile/     — app móvil (React Native + Expo) — aún no iniciada
apps/admin/      — panel administrativo (React + Vite) — aún no iniciado
backend/         — API REST (Django + DRF + PostGIS)
infrastructure/  — Docker y scripts
docs/            — documentación del proyecto
```

## Cómo empezar

Ver `docs/INSTALLATION.md` para levantar el backend paso a paso.

```bash
docker compose up -d db
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example ../.env   # y edítalo
python manage.py migrate
python manage.py runserver
curl http://localhost:8000/api/v1/health/
```
