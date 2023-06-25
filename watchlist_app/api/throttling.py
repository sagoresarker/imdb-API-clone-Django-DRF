from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class ReviewCreateThrotte(UserRateThrottle):
    scope = 'review-create'

class ReviewListThrotte(UserRateThrottle):
    scope = 'review-list'