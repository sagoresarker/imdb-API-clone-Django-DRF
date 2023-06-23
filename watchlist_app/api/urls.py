from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailsAV.as_view() , name='movie-details'),
    
    path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', views.StreamPlatformDetailsViewAV.as_view(), name='stream-details'),
    path('stream/pythreview/<int:pk>', views.ReviewDetail.as_view(), name='review-details'),
    
    # path('review/', views.ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', views.ReviewDetail.as_view(), name='review-list'),
    
    path('stream/<int:pk>/review', views.ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'),

    path('stream/<int:pk>/review-create', views.ReviewCreate.as_view(), name='review-create'),
]