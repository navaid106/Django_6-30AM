from django.shortcuts import render
from django.http import HttpResponse, JsonResponse



# 1. place_order
# 2. order_history

def place_order(request):
    return HttpResponse('<h1>Order Placed successfully!</h1>')

def order_history(request):
    orders = [
        {'id':1,'item':'Laptop', 'status':'Delivered'},
        {'id':2,'item':'Mouse', 'status':'Pending'}
    ]
    dict = {'orders':orders}
    return JsonResponse(dict)