# Instalación — Ojo Ciudadano (Etapa 1)

Esta guía cubre lo que ya existe: el backend Django conectado a una
base de datos PostgreSQL con PostGIS. Las apps móvil y de panel
administrativo se agregan en etapas posteriores.

## Requisitos

- Python 3.11+ (se probó con 3.13)
- PostgreSQL 16 con la extensión PostGIS 3.4
- Git

En Windows/Mac, lo más simple es usar **Docker Desktop** y el
`docker-compose.yml` de la raíz (`docker compose up -d db`), que
descarga la imagen oficial `postgis/postgis:16-3.4`.

> En el entorno donde se construyó este proyecto por primera vez no
> había salida a internet para descargar imágenes de Docker, así que
> se instaló PostgreSQL + PostGIS directamente con `apt`. Si tu
> computador sí tiene internet, usa Docker Compose: es más simple y
> no ensucia tu sistema con PostgreSQL instalado de forma nativa.

## 1. Base de datos

### Opción A — Docker (recomendada)

```bash
docker compose up -d db
```

Esto expone PostgreSQL en `localhost:5432` con la base `ojo_ciudadano`,
usuario `ojo_user`, clave `ojo_pass` (ver `docker-compose.yml`).

### Opción B — PostgreSQL instalado localmente

```bash
sudo apt install postgresql-16 postgresql-16-postgis-3 postgis gdal-bin libgdal-dev

sudo -u postgres psql
CREATE USER ojo_user WITH PASSWORD 'ojo_pass';
CREATE DATABASE ojo_ciudadano OWNER ojo_user;
\c ojo_ciudadano
CREATE EXTENSION postgis;
```

> **Solo en desarrollo local:** para que `python manage.py test` pueda
> crear su base de datos de prueba y habilitar PostGIS en ella, el
> usuario necesita permisos de superusuario de Postgres:
> `ALTER USER ojo_user WITH SUPERUSER;`. En un servidor real, la
> extensión PostGIS se instala una sola vez con un usuario
> administrador y la aplicación se conecta con un usuario normal, sin
> ese permiso.

## 2. Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Copia el archivo de variables de entorno (vive en la raíz del
repositorio, no dentro de `backend/`):

```bash
cp ../.env.example ../.env
```

Ajusta `DJANGO_SECRET_KEY` (genera una nueva) y, si usaste la Opción B
de arriba, confirma que `DATABASE_URL` coincide con tu usuario/clave.

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 3. Verificar que todo funciona

```bash
curl http://localhost:8000/api/v1/health/
```

Debe responder algo como:

```json
{"status": "ok", "service": "ojo-ciudadano-backend", "database": "connected", "postgis_version": "3.4 ..."}
```

También puedes entrar a `http://localhost:8000/admin/` con el
superusuario que creaste, y a `http://localhost:8000/api/v1/docs/`
para ver la documentación OpenAPI (todavía vacía: los endpoints de
negocio llegan en la Etapa 3).

## 4. Pruebas automatizadas

```bash
python manage.py test
```

## Problemas comunes

- **`permission denied to create extension "postgis"`** al correr los
  tests: tu usuario de Postgres no es superusuario. Ver la nota de la
  sección 1, Opción B.
- **`libgdal.so: cannot open shared object file`**: faltan las
  librerías nativas de GeoDjango. Instala `gdal-bin libgdal-dev
  libgeos-dev libproj-dev` (en Ubuntu/Debian) o el paquete
  equivalente de tu sistema.
- **La app móvil no puede conectarse al backend desde un celular
  físico**: no uses `localhost` en el celular (apuntaría al propio
  teléfono). Usa la IP de tu computador en la red local, y agrégala a
  `ALLOWED_HOSTS` y `CORS_ALLOWED_ORIGINS` en `.env`. Esto se detalla
  más en la Etapa 4.
