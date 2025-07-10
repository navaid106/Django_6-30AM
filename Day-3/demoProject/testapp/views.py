from django.shortcuts import render
from django.http import HttpResponse

def demo_view(request):
    return HttpResponse("Welcome To Django Class...")


def home_view(request):
    return HttpResponse("This is Home Page...")


def about_view(request):
    return HttpResponse("This is About Page...")