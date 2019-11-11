from django.shortcuts import render
from rest_framework import viewsets
from .models import test_db
from .serializers import TestSerializer

class TestViewset(viewsets.ModelViewSet):
    queryset = test_db.objects.order_by("-id")
    serializer_class = TestSerializer