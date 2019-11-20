from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings
from .models import test_db
from .serializers import TestSerializer
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    posts_list = test_db.objects.order_by('-id')

    page_size = api_settings.PAGE_SIZE
    paginator = Paginator(posts_list,page_size)

    page = request.GET.get('page')
    
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    return render(request, 'for_test/index.html', { 'posts' : posts })