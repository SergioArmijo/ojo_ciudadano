
from django.db import models


class Category(models.Model):
    name = models.CharField("Nombre", max_length=100, unique=True)
    description = models.TextField("Descripción", blank=True)
    is_active = models.BooleanField("Activa", default=True)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]

    def __str__(self):
        return self.name
