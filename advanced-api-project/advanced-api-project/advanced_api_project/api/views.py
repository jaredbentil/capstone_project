# api/views.py
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Make sure you have installed and added 'django_filters' to INSTALLED_APPS in settings.py
from django_filters.rest_framework import DjangoFilterBackend 

# NOTE: These imports assume you have Book model in api/models.py 
# and BookSerializer in api/serializers.py
from .models import Book 
from .serializers import BookSerializer 

# --- Collection Endpoint (List & Create) ---
class BookListCreate(generics.ListCreateAPIView):
    """
    Handles GET (list all books) and POST (create a new book), 
    with support for filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    
    # --- Integrate Filter Backends (Required for Filtering, Searching, Ordering) ---
    filter_backends = [
        DjangoFilterBackend,  # Step 1: Filtering by exact match
        filters.SearchFilter, # Step 2: Text search
        filters.OrderingFilter, # Step 3: Ordering/Sorting
    ]
    
    # --- Step 1: Filtering Configuration ---
    # Allows filtering by exact match on these fields.
    filterset_fields = ['title', 'author', 'publication_year'] 
    
    # --- Step 2: Search Configuration ---
    # Allows full-text search across these fields.
    search_fields = ['title', 'author'] 
    
    # --- Step 3: Ordering Configuration ---
    # Allows ordering results by these fields using the 'ordering' query param.
    ordering_fields = ['title', 'publication_year', 'author']
    ordering = ['title'] 


# --- Instance Endpoint (Retrieve, Update, and Delete) ---
class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (detail), PUT/PATCH (update), and DELETE (destroy) for a single book.
    Permissions: Requires authentication for all operations.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]