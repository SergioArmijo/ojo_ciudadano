
from django.contrib import admin

from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "status",
        "created_by",
        "created_at",
    )
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "description", "address")
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 25
