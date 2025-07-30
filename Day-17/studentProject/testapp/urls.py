from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_view, name='student-view'),
    path('api/students/', views.student_json_view, name='student-json'),
]
