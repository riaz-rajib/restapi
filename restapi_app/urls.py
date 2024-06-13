from django.urls import path
from . import views

urlpatterns = [
    path('api/albums', views.album_list),
    path('api/albums/<int:pk>', views.album_details),
    path('api/tracks', views.track_list),
]