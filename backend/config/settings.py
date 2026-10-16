"""
Configuración de Django para Ojo Ciudadano.

Lee sus valores desde variables de entorno (ver .env.example en la raíz
del repositorio). Nunca hay secretos escritos directamente aquí.
"""

from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DJANGO_DEBUG=(bool, False),
)
# El .env vive en la raíz del repositorio (un nivel arriba de backend/).
environ.Env.read_env(BASE_DIR.parent / ".env")

SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-insecure-solo-para-desarrollo-local")
DEBUG = env.bool("DJANGO_DEBUG", default=True)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])


# --- Aplicaciones ---

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",  # GeoDjango, necesario para los campos geográficos (PostGIS)
    # Terceros
    "rest_framework",
    "corsheaders",
    "drf_spectacular",
    # Apps propias de Ojo Ciudadano
    "apps.accounts",
    "apps.categories",
    "apps.organizations",
    "apps.reports",
    "apps.evidence",
    "apps.assignments",
    "apps.notifications",
    "apps.chatbot",
    "apps.audit",
]

AUTH_USER_MODEL = "accounts.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# --- Base de datos ---
# DATABASE_URL en .env, ej: postgis://usuario:clave@host:5432/nombre_bd

DATABASES = {
    "default": env.db_url(
        "DATABASE_URL",
        default="postgis://ojo_user:ojo_pass@localhost:5432/ojo_ciudadano",
    )
}


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# --- CORS ---
# Orígenes del panel admin (Vite) y de la app móvil (Expo) en desarrollo.
CORS_ALLOWED_ORIGINS = env.list(
    "CORS_ALLOWED_ORIGINS",
    default=["http://localhost:5173", "http://localhost:19006"],
)


# --- Django REST Framework ---
# Nota: la autenticación por tokens (JWT) para la app móvil y el panel se
# implementa en la Etapa 2. Por ahora, solo autenticación por sesión (útil
# para el admin de Django y para verificar el backend desde el navegador).
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Ojo Ciudadano API",
    "DESCRIPTION": "API REST para el sistema de reportes ciudadanos de Pereira.",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
