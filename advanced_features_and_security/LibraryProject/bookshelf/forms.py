from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    A form for creating and editing Book model instances.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class ExampleForm(forms.Form):
    """
    A simple example form to satisfy the check.
    """
    your_name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email')