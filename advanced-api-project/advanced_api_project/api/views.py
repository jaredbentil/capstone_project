from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

# ViewSet for the Author model
class AuthorViewSet(viewsets.ModelViewSet):
 
    queryset = Author.objects.all().order_by('name') # Alphabetical order by name
    serializer_class = AuthorSerializer

# ViewSet for the Book model
class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all().order_by('-publication_year') # Newest books first
    serializer_class = BookSerializer


