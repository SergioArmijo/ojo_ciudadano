
from django.conf import settings
from django.contrib.gis.db import models as gis_models
from django.db import models


class Report(models.Model):
    class Status(models.TextChoices):
        RECEIVED = "received", "Recibido"
        IN_REVIEW = "in_review", "En revisión"
        IN_PROGRESS = "in_progress", "En atención"
        RESOLVED = "resolved", "Resuelto"
        REJECTED = "rejected", "Rechazado"

    title = models.CharField("Título", max_length=150)
    description = models.TextField("Descripción")
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.PROTECT,
        related_name="reports",
        verbose_name="Categoría",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="citizen_reports",
        verbose_name="Creado por",
    )
    location = gis_models.PointField(
        "Ubicación",
        geography=True,
        srid=4326,
    )
    address = models.CharField("Dirección o referencia", max_length=255, blank=True)
    status = models.CharField(
        "Estado",
        max_length=20,
        choices=Status.choices,
        default=Status.RECEIVED,
    )
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Última actualización", auto_now=True)

    class Meta:
        verbose_name = "Reporte ciudadano"
        verbose_name_plural = "Reportes ciudadanos"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
