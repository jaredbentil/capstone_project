from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import PostViewSet, CommentViewSet, FeedView

# Main router for Posts
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Nested router for Comments within Posts
# This creates URLs like /posts/{post_pk}/comments/
posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'), #feed URL
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
    path('<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='like-post'),
    path('<int:pk>/unlike/"]', PostViewSet.as_view({'post': 'unlike'}), name='unlike-post'),    
]
