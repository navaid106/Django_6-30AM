from django.shortcuts import render
from testapp.forms import StudentForm


def register(request):
    # craete form object.

    # 1. for empty form or for filled form
    form = StudentForm(request.POST or None)

    # check POST request and is_valid() data
    if request.method == "POST" and form.is_valid():
        # 1. print form data on console screen

        # Syntax: cleaned_data['field_name']
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        desc = form.cleaned_data['description']

        print(f'Name: {name}')
        print(f'Email: {email}')
        print(f'Description: {desc}')

        # 2. send form data to html page.
        data_dict = {
            'name':name,
            'email':email,
            'desc':desc
        }

        return render(request, 'testapp/data.html',{'data_dict':data_dict})

    return render(request, 'testapp/student.html',{'form':form})   

    
