from django.contrib import admin
from django.urls import path,include

# Project level URLS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/',include('order.urls')),
    path('product/',include('product.urls')),
    path('customer/',include('customer.urls'))
]
