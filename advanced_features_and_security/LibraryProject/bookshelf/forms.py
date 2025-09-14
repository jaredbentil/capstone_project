from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    A form for creating and editing Book model instances.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']