from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

# Create your views here.
# Create Two views

# 1. product_list
# 2. product_details

def product_list(request):
    data = ['Laptop','Mouse','Keyboard']
    dict = {'data':data}

    return JsonResponse(dict)

def product_details(request,product_id):
    details = f"""
            <h1 style='color:crimson'>Product Detail for Product ID: {product_id}</h1>
        """
    
    return HttpResponse(details)
