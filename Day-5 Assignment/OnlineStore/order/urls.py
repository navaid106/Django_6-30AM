from django.urls import path
from order import views

urlpatterns = [
    path('place/',views.place_order),
    path('history/',views.order_history),
]