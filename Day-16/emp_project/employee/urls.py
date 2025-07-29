from django.urls import path
from employee import views

urlpatterns = [
    path('',views.home),
    path('employees/', views.employee_list, name='employee_list'),
    path('api/employees/', views.employee_api, name='employee_api'),
]
