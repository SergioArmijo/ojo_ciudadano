"""
Rutas raíz de Ojo Ciudadano.

Los endpoints de negocio (reportes, categorías, chatbot, etc.) se
agregan en etapas posteriores, cada uno dentro de su propia app bajo
/api/v1/. Por ahora solo existen:
- /admin/            -> administración de Django, útil para depurar.
- /api/v1/health/     -> endpoint de verificación (backend + base de datos).
- /api/v1/schema/     -> esquema OpenAPI generado por drf-spectacular.
- /api/v1/docs/       -> documentación interactiva (Swagger UI).
"""

from django.contrib import admin
from django.db import connection
from django.http import JsonResponse
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


def health(request):
    """
    Verifica que el backend responde y que la base de datos (con
    PostGIS) está accesible. Útil para confirmar que la Etapa 1
    quedó correctamente conectada.
    """
    db_ok = False
    postgis_version = None
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT PostGIS_Version();")
            postgis_version = cursor.fetchone()[0]
            db_ok = True
    except Exception as exc:  # noqa: BLE001 - se reporta el error, no se oculta
        return JsonResponse({"status": "error", "database": str(exc)}, status=503)

    return JsonResponse(
        {
            "status": "ok",
            "service": "ojo-ciudadano-backend",
            "database": "connected" if db_ok else "unavailable",
            "postgis_version": postgis_version,
        }
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/health/", health, name="health"),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
