from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

# ViewSet for the Author model
class AuthorViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Author instances.
    Uses AuthorSerializer which features nested Book serialization.
    """
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer

# ViewSet for the Book model
class BookViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Book instances.
    Uses BookSerializer which includes custom validation on publication_year.
    """
    queryset = Book.objects.all().order_by('-publication_year')
    serializer_class = BookSerializer
