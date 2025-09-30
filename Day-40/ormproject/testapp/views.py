from django.shortcuts import render

from testapp.models import Employee

def retrieve_view(request):
    # ORM Queries to fetch database records..

    # Fetch all the records 
    # emp_list = Employee.objects.all() # select * from Employee

    # emp_list = Employee.objects.get()

    # fetch employee records based condtion
    # gt, gte, lt, lte
    # emp_list = Employee.objects.filter(esal__gte=15000)

    # Contains:
    # select ... where name like %john%
    # emp_list = Employee.objects.filter(ename__contains='Smith')

    # emp_list = Employee.objects.filter(id__in=[1,3])

    # emp_list = Employee.objects.filter(ename__startswith='d')
    emp_list = Employee.objects.filter(ename__endswith='d')

    



    return render(request, 'testapp/index.html',{'emp_list':emp_list})


