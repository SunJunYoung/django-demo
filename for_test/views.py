from django.shortcuts import render
from rest_framework import viewsets
from .models import test_db
from .serializers import TestSerializer
from datetime import datetime

class TestViewset(viewsets.ModelViewSet):
    queryset = test_db.objects.order_by("-id")
    serializer_class = TestSerializer

    def create(self, request):
        # print transaction time if headers have Timestamp attribute
        if 'Timestamp' in request.headers:
            transaction_time = float(datetime.now().timestamp()) - float(request.headers['Timestamp'])
            print("transaction time: {0}".format(transaction_time))
        return super().create(request)

def indexView(request):
    posts = test_db.objects.order_by('-id')
    return render(request, 'for_test/index.html', { 'posts' : posts })