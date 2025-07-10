
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('text/',views.text_view),
    path('html/',views.html_view),
    path('json/',views.json_view),
]
