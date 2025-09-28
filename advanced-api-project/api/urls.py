from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# The router is used for the Author ViewSet.
router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet, basename='author')

# Manual URL patterns for each specific Book view.
urlpatterns = [
    # URLs for the Author ViewSet
    path('', include(router.urls)),

    # URLs for Book CRUD operations
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]

