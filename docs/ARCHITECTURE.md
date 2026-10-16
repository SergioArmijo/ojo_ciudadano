# Arquitectura — Ojo Ciudadano

## Visión general (objetivo final)

```
App móvil (Expo) ──┐
                    ├─► Backend Django REST (/api/v1/) ──► PostgreSQL + PostGIS
Panel admin (Vite) ─┘                │
                                     └─► OjoBot (proveedor de IA, solo desde el backend)
```

## Estado actual (Etapa 1)

Solo existe el backend y la base de datos:

- **Backend:** Django 5 + Django REST Framework, en `backend/`.
  Apps internas bajo `backend/apps/`: `accounts`, `reports`,
  `categories`, `evidence`, `organizations`, `assignments`,
  `notifications`, `chatbot`, `audit`. Hoy solo `accounts` tiene un
  modelo real (`User`); las demás son esqueletos vacíos listos para
  la Etapa 2 en adelante.
- **Base de datos:** PostgreSQL 16 con PostGIS 3.4, para poder guardar
  la ubicación de cada reporte como un punto geográfico real (no como
  dos números sueltos de latitud/longitud).
- **Documentación de API:** generada automáticamente por
  drf-spectacular en `/api/v1/schema/` y `/api/v1/docs/`, a medida que
  se agregan endpoints.

## Decisiones tomadas

- **Usuario personalizado desde el inicio** (`apps.accounts.User`):
  Django no permite cambiar el modelo de usuario después de la
  primera migración sin complicaciones, así que se definió desde la
  Etapa 1 con un campo `role`, aunque los permisos por rol se
  implementan en la Etapa 2.
- **PostGIS en vez de campos lat/lng sueltos:** permite hacer
  consultas geográficas reales (reportes dentro de un radio, por
  barrio, etc.) en la Etapa 5.
