from django.shortcuts import render
from testapp.models import Employee 
from rest_framework import generics
from testapp.serializers import EmployeeSerializer

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializer



