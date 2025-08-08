
from django.urls import path
from testapp import views

urlpatterns = [
    path('student/',views.student_view),
    path('student/api/',views.student_json_view),
]