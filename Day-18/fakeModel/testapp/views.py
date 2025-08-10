from django.shortcuts import render
from testapp.models import Student
from django.http import JsonResponse


def student_view(request):
    # sql: select * from Student
    # orm: Student.objects.all()

    students = Student.objects.all()

    return render(request, 'testapp/index.html',{'students':students})


def student_json_view(request):
    students = Student.objects.all().values()

    student_list = list(students)

    return JsonResponse({'student_list':student_list})