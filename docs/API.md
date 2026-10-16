# API — Ojo Ciudadano

Todavía no hay endpoints de negocio. Lo único disponible hoy:

| Método | Ruta                | Descripción                                    |
|--------|---------------------|-------------------------------------------------|
| GET    | `/api/v1/health/`   | Verifica que el backend y PostGIS responden.    |
| GET    | `/api/v1/schema/`   | Esquema OpenAPI (JSON).                         |
| GET    | `/api/v1/docs/`     | Documentación interactiva (Swagger UI).         |

Los endpoints de autenticación, reportes, categorías, administración
y OjoBot se documentan aquí a medida que se implementan (Etapas 2 a
8), siguiendo el prefijo `/api/v1/` para todos.
