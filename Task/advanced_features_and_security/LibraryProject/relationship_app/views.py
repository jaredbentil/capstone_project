from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required

from .models import Book, Library, Library_books

# relationship_app/views.py

def home(request):
    """
    Renders the home page of the application.
    """
    return render(request, "relationship_app/home.html")

# -------------------------------
# Function-based view to list all books
# -------------------------------
def list_books(request):
    """
    Retrieves all Book objects from the database and renders a list view.
    """
    books = Book.objects.all()
    # Explicit template path
    return render(request, "relationship_app/list_books.html", {"books": books})

# -------------------------------
# Class-based view for BookForm
# -------------------------------
class BookForm(forms.ModelForm):
    """
    A form for creating or updating a Book instance.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class LibraryDetailView(DetailView):
    """
    A class-based view to display details of a single Library.
    """
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Registration view
def register(request):
    """
    Handles user registration and logs the user in upon successful creation.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in right after registration
            return redirect("list_books")  # redirect to any page, e.g., book list
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# --- Helpers for role checks ---
def is_admin(user):
    """
    Checks if a user is an admin.
    """
    return hasattr(user, "profile") and user.profile.role == "Admin"

def is_librarian(user):
    """
    Checks if a user is a librarian.
    """
    return hasattr(user, "profile") and user.profile.role == "Librarian"

def is_member(user):
    """
    Checks if a user is a regular member.
    """
    return hasattr(user, "profile") and user.profile.role == "Member"


# --- Role-based views ---
@user_passes_test(is_admin)
@login_required
def admin_view(request):
    """
    A view accessible only to admin users.
    """
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    """
    A view accessible only to librarian users.
    """
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
@login_required
def member_view(request):
    """
    A view accessible only to member users.
    """
    return render(request, "relationship_app/member_view.html")

# Add book view
@permission_required('relationship_app.can_add_book')
def add_book(request):
    """
    Handles adding a new book, requiring specific permissions.
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

# Edit book view
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    """
    Handles editing an existing book, requiring specific permissions.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form, "book": book})

# Delete book view
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    """
    Handles deleting a book, requiring specific permissions.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    return render(request, "relationship_app/delete_book.html", {"book": book})

