from django.urls import path
from testapp import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('news/<str:category>/',views.news_view, name='news'),
]