from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    """Roles del sistema (sección 4 del documento de especificación)."""

    SUPERADMIN = "superadmin", "Superadministrador"
    ADMIN = "admin", "Administrador"
    OPERADOR = "operador", "Operador"
    AUDITOR = "auditor", "Auditor"
    CIUDADANO = "ciudadano", "Ciudadano"


class User(AbstractUser):
    """
    Usuario del sistema. Extiende el modelo de Django (que ya trae
    contraseña con hash seguro, email, fechas, etc.) y le agrega los
    campos propios de Ojo Ciudadano.

    La lógica de permisos por rol se implementa en la Etapa 2, en
    `apps/accounts/permissions.py`. Ocultar botones en la interfaz NO
    es un mecanismo de seguridad: todo permiso se valida en el backend.
    """

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CIUDADANO,
        help_text="Rol funcional del usuario dentro del sistema.",
    )
    is_account_active = models.BooleanField(
        default=True,
        help_text="Permite suspender una cuenta sin eliminarla.",
    )
    notify_by_email = models.BooleanField(default=True)
    notify_by_push = models.BooleanField(default=True)
    last_activity_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.get_full_name() or self.username
