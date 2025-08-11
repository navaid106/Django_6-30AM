
from django.contrib import admin
from django.urls import path
from testapp import views
from django.conf.urls.static import static
from mediaProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/',views.course_view)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 1. MEDIA_URL [name of teh shop where people visit]
# 2. document_root [storeroom where the goods(images) are actually kept]
