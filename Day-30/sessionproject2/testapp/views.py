from django.shortcuts import render


def home_view(request):
    return render(request,'testapp/home.html')


def age_view(request):
    print(request.COOKIES)
    username = request.GET['name']
   
    response = render(request,'testapp/age.html',{'name':username})
    response.set_cookie('name',username)

    return response


def course_view(request):
    print(request.COOKIES)
    username = request.COOKIES['name']
    age = request.GET['age']

    response = render(request,'testapp/course.html',{'name':username})
    response.set_cookie('age',age)

    return response


def result_view(request):
    print(request.COOKIES)
    username = request.COOKIES['name']
    age = request.COOKIES['age']
    course = request.GET['course']

    response = render(request,'testapp/results.html',{'name':username, 'age':age,'course':course})

    return response
