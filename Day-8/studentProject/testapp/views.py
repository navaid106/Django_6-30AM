from django.shortcuts import render

def student_data(request):
    student_profile = {
        # key:value

        'name':'Nobita',
        'age':25,
        'course':'Python Full Stack Developer'

    }

    return render(request,'testapp/index.html',context=student_profile)
