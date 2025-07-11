from django.urls import path
from order import views

# Application Level URLS
urlpatterns = [
    path('place/',views.place_order),
    path('history/',views.order_history),
]