from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api import views
from .views import BookListCreate, BookRetrieveUpdateDestroy

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-detail-update-delete'),
         
]




