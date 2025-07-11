from django.urls import path
from customer import views

# Application Level URLS
urlpatterns = [
    path('profile/',views.profile),
    path('dashboard/',views.dashboard),
]