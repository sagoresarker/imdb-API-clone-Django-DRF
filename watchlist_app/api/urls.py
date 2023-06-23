from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailsAV.as_view() , name='movie-details'),
    path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', views.StreamPlatformDetailsViewAV.as_view(), name='stream-details'),
]