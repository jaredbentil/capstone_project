from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# --- Author ViewSet (No changes needed here) ---
# We can keep the ViewSet for Authors as it provides full CRUD functionality automatically.
from rest_framework import viewsets

class AuthorViewSet(viewsets.ModelViewSet):
  
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # You could add permissions here as well, for example:
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# --- Book Generic Views (Fulfills the new task requirements) ---

class BookListCreateView(generics.ListCreateAPIView):
   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]