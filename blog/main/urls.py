from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path("aside/", LastPostsView.as_view()),
    path('tags/', TagView.as_view()),
    path('tags/<slug:tag_slug>/', TagDetailView.as_view()),
    path("feedback/", FeedBackView.as_view()),
    path('signup/', SignupView.as_view()),
    path('profile/', UserView.as_view()),
]