
from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    class Meta:
        model = Report
        fields = [
            "id",
            "title",
            "description",
            "category",
            "category_name",
            "created_by",
            "location",
            "address",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_by",
            "created_at",
            "updated_at",
        ]
