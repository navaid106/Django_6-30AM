from django.urls import path
from movies import views

urlpatterns = [
    # Note: for each endpoint we have to create a view
    path('', views.home_view),
    path('movies/',views.movie_list_view),
    path('movies/<int:id>/',views.movie_detail_view),
    path('api/movies/',views.movie_json_view)

]