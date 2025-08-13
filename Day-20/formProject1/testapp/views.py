from django.shortcuts import render
from testapp.forms import StudentForm


def student_input_view(request):
    forms = StudentForm()

    return render(request,'testapp/student.html',{'forms':forms})

