from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# --- Author ViewSet (Provides full CRUD automatically) ---
class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# --- Book Generic Views (Implemented as 5 separate classes) ---

class BookListView(generics.ListAPIView):
    """
    (ListView) Handles GET requests to list all books.
    - Allows read-only access to all users (authenticated or not).
    - Supports filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    
    # --- Step 1, 2, 3: Configure Filtering, Searching, and Ordering ---
    # Explicitly define which filter backends this view should use.
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Step 1: Filtering Configuration
    # Connects to DjangoFilterBackend
    # e.g., /api/books/?publication_year=1949
    filterset_fields = ['publication_year', 'author']
    
    # Step 2: Search Configuration
    # Connects to SearchFilter
    # e.g., /api/books/?search=orwell
    search_fields = ['title', 'author__name']
    
    # Step 3: Ordering Configuration
    # Connects to OrderingFilter
    # e.g., /api/books/?ordering=-publication_year (descending)
    ordering_fields = ['publication_year', 'title']


class BookDetailView(generics.RetrieveAPIView):
    """
    (DetailView) Handles GET requests to retrieve a single book by its ID.
    - Allows read-only access to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    (CreateView) Handles POST requests to create a new book.
    - Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    (UpdateView) Handles PUT and PATCH requests to update an existing book.
    - Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    (DeleteView) Handles DELETE requests to remove a book.
    - Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

