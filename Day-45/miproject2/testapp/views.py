from django.shortcuts import render


from testapp.models import Employee

def display_view(request):
    emp_list = Employee.objects.all()
   
    print(type(Employee.objects))
    print(type(emp_list))

    return render(request,'testapp/index.html',{'emp_list':emp_list})

