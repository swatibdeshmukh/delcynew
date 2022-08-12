
from django.shortcuts import render
from delapp.models import *
from delapp.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class EmployeeDetails(viewsets.ViewSet):
    def list(self, request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def create(self,request):
    #     serializer = EmployeeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)