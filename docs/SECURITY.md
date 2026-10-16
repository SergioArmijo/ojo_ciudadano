# Seguridad — Ojo Ciudadano

## Vigente desde la Etapa 1

- Las contraseñas se guardan con el hash seguro por defecto de
  Django (PBKDF2), nunca en texto plano.
- El secreto de Django (`DJANGO_SECRET_KEY`) y las credenciales de
  base de datos viven en `.env`, que está excluido de git
  (`.gitignore`). El repositorio solo versiona `.env.example`, sin
  valores reales.
- `DEBUG` debe quedar en `False` en producción (variable
  `DJANGO_DEBUG`), para no exponer trazas internas de error.

## Pendiente (etapas siguientes)

- Autenticación con expiración/renovación de tokens y permisos por
  rol y por objeto (Etapa 2).
- Límite de tamaño y tipo de archivo, y revisión de evidencias
  potencialmente maliciosas (Etapa 5).
- CORS y CSRF ajustados para producción, límites de solicitudes y
  registro de auditoría de acciones administrativas (Etapa 9).
- Cumplimiento de la Ley 1581 de 2012 (protección de datos
  personales) en el manejo de evidencias e identidad de quien
  reporta.
