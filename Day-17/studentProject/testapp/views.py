from django.shortcuts import render
from django.http import JsonResponse
from testapp.models import Student

def student_view(request):
    student_list = Student.objects.all()
    return render(request, 'testapp/std.html', {'student_list': student_list})

def student_json_view(request):
    data = list(Student.objects.values())
    return JsonResponse(data, safe=False)