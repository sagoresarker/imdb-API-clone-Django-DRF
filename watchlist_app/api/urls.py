from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailsAV.as_view() , name='movie-details'),
    
    path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', views.StreamPlatformDetailsViewAV.as_view(), name='stream-details'),
    path('stream/pythreview/<int:pk>/', views.ReviewDetail.as_view(), name='review-details'),
    
    # path('review/', views.ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', views.ReviewDetail.as_view(), name='review-list'),
    
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),

    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    # path('reviews/<str:username>/', views.UserReview.as_view(), name='user-review-detail'),
    path('reviews/', views.UserReview.as_view(), name='user-review-detail'),
]