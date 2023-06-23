from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    path('list/', views.MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.MovieDetailsAV.as_view() , name='movie-details'),
]