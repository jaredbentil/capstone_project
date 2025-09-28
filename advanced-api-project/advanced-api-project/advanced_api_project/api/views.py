# api/views.py (The Recommended Corrected Version)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# --- ViewSet for Author (Handles List, Create, Retrieve, Update, Destroy) ---
class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    Requires authentication for creation/modification.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # Allow anyone to view (GET), but require authentication to create/update/delete.
    permission_classes = [IsAuthenticatedOrReadOnly] 
    
    # NOTE: No need to define separate list/detail/create methods, ModelViewSet does it for you.


# --- ViewSet for Book (Handles List, Create, Retrieve, Update, Destroy) ---
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Customization Example: Filter books by author if a query parameter is provided
    # ModelViewSet uses get_queryset() just like the generic views
    def get_queryset(self):
        queryset = super().get_queryset()
        author_name = self.request.query_params.get('author', None)
        
        if author_name is not None:
            # Assumes 'Author' model has a 'name' field
            # Filters books where the author's name contains the query string (case-insensitive)
            queryset = queryset.filter(author__name__icontains=author_name)
            
        return queryset