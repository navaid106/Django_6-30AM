from django.shortcuts import render
from testapp.models import Course

def course_view(request):
    courses = Course.objects.all()

    return render(request,'testapp/index.html',{'courses':courses})
