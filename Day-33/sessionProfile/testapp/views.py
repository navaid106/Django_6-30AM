from django.shortcuts import render
from testapp.forms import NameForm, AgeForm,CourseForm


def name_view(request):
    form = NameForm()
    return render(request,'testapp/name.html',{'form':form})

def age_view(request):
    name = request.GET['name']
    request.session['name'] = name

    form = AgeForm()

    return render(request, 'testapp/age.html',{'form':form,'name':name})

def course_view(request):
    age = request.GET['age']
    request.session['age'] = age
    name = request.session['name']
    form = CourseForm()

    return render(request,'testapp/course.html',{'form':form,'name':name})


def result_view(request):
    course = request.GET['course']
    request.session['course'] = course
    name = request.session['name']
    age = request.session['age']

    return render(request,'testapp/results.html')


