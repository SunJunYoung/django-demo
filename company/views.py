import datetime
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CompanySerializer
from .models import Company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.order_by("-SEQ")
    serializer_class = CompanySerializer
    lookup_field = 'SEQ'

    def create(self, request):
        # print transaction time if headers have Timestamp attribute
        if 'Timestamp' in request.headers:
            transaction_time = float(datetime.now().timestamp()) - float(request.headers['Timestamp'])
            print("transaction time: {0}".format(transaction_time))
        # Check if request body is mulitple data or not.
        many = False
        if type(request.data) == list:
            many = True
        serializer = CompanySerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)