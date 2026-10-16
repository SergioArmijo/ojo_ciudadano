
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Report
from .serializers import ReportSerializer


class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.select_related("category").all()
    serializer_class = ReportSerializer
    permission_classes = [AllowAny]
