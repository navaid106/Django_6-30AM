from django.contrib import admin
from django.urls import path

from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.demo_view),
    path('home/',views.home_view),
    path('about/',views.about_view)
]
