from django.shortcuts import render
from django.http import HttpResponse

def welcome_view(request):
    print('This line is added by view function')
    return HttpResponse('<h1>Custom Middleware Demo</h1>')
