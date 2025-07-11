from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.

# 1. profile
# 2. dashboard


def profile(request):

    customer_profile ={
        # key:value

        'name':'Doreamon',
        'email':'dora@gmail.com',
        'membership':'Permium',
    }

    return JsonResponse(customer_profile)


def dashboard(request):
    customer_dashboard = """
        <h1 style='color:violet; font-size:60px'> 
            Welcome to Customer Dashboard...
        </h1>
    """

    return HttpResponse(customer_dashboard)