from django.shortcuts import render
from employee.models import Employee
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request, 'employee/home.html')

def employee_list(request):
    # select * from employee <==> employee.objects.all()
    # employee.objects.all()
    employee = Employee.objects.all()

    dict = {
        'employee':employee
    }

    return render(request, 'employee/emp_list.html',dict)


def employee_api(request):
    employee = Employee.objects.all().values('id','name','department')
    return JsonResponse(list(employee),safe=False)
