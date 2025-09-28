from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# The router is still great for the full AuthorViewSet
router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet, basename='author')

# For our new generic views, we define the URL patterns manually.
urlpatterns = [
    # URLs for the Author ViewSet are handled by the router
    path('', include(router.urls)),

    # URL for listing all books or creating a new book
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),

    # URL for retrieving, updating, or deleting a single book by its primary key (pk)
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]
