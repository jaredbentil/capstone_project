from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .models import Author, Book
from django_filters import rest_framework as filters
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
    
    # Integrate filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtering Configuration
    filterset_fields = ['publication_year', 'author']
    
    # Search Configuration
    search_fields = ['title', 'author__name']
    
    # Ordering Configuration
    ordering_fields = ['publication_year', 'title']


class BookDetailView(generics.RetrieveAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookCreateView(generics.CreateAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

