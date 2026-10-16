from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        (
            "Ojo Ciudadano",
            {
                "fields": (
                    "role",
                    "is_account_active",
                    "notify_by_email",
                    "notify_by_push",
                    "last_activity_at",
                )
            },
        ),
    )
    list_display = ("username", "email", "role", "is_account_active", "is_staff")
    list_filter = DjangoUserAdmin.list_filter + ("role", "is_account_active")
