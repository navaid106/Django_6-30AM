from django.urls import path
from product import views

# Application Level URLS
urlpatterns = [
    path('',views.product_list),
    path('<int:product_id>',views.product_details),
]