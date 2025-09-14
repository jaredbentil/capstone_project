from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Book

# This is the view for displaying a list of books.
def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})

# This is the view for user registration.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login') # Redirect to a login page
    else:
        form = UserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})

# This view requires the 'can_create' permission.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # This is placeholder code. You will need to add a form and logic.
    return render(request, 'bookshelf/create_book.html')

# This view requires the 'can_edit' permission.
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # This is placeholder code. You will need to add a form and logic.
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# This view requires the 'can_delete' permission.
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # This is placeholder code. You will need to add a form and logic.
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')