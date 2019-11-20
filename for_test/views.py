from django.shortcuts import render
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
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
        # Check if request body is mulitple data or not.
        many = False
        if type(request.data) == list:
            many = True
        serializer = TestSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def indexView(request):
    posts = test_db.objects.order_by('-id')
    return render(request, 'for_test/index.html', { 'posts' : posts })
