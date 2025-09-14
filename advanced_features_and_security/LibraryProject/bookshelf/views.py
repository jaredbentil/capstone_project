from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm 

# This is the view for displaying a list of books.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# This is the view for user registration.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})

# This view handles searching for books.
def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) # Using the ORM to prevent SQL injection
    return render(request, 'bookshelf/book_list.html', {'books': books})

# The following views require specific permissions.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Add your form and logic for creating a book here
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # Add your form and logic for editing a book here
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # Add your logic for deleting a book here
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')