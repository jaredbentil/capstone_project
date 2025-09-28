

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend # Required for advanced filtering
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# --- 1. Author ViewSet (Simple CRUD) ---
class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Authors to be viewed, created, updated, or deleted.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # Allows GET (Read) to anyone, requires authentication for POST, PUT, PATCH, DELETE.
    permission_classes = [IsAuthenticatedOrReadOnly]


# --- 2. Book ViewSet (CRUD + Advanced Filtering/Searching/Ordering) ---
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Books to be viewed, created, updated, or deleted.
    Includes support for filtering, searching, and ordering via query parameters.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # --- Integrate Filter Backends into the ViewSet ---
    filter_backends = [
        DjangoFilterBackend,  # 1. Filtering by exact match (e.g., ?author=1)
        filters.SearchFilter, # 2. Text search (e.g., ?search=Lord)
        filters.OrderingFilter, # 3. Ordering/Sorting (e.g., ?ordering=-publication_year)
    ]
    
    # --- Filtering Configuration (DjangoFilterBackend) ---
    filterset_fields = ['title', 'author', 'publication_year'] 
    
    # --- Search Configuration (filters.SearchFilter) ---
    search_fields = ['title', 'author__name'] # Assuming author is a foreign key with a 'name' field
    
    # --- Ordering Configuration (filters.OrderingFilter) ---
    ordering_fields = ['title', 'publication_year', 'author']
    ordering = ['title'] # Default ordering

    # NOTE: The custom get_queryset for filtering by author is no longer needed 
    # as the 'DjangoFilterBackend' and 'filterset_fields' handle that more flexibly.