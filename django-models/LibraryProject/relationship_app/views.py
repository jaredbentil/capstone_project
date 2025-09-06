from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library
from .models import Library

# relationship_app/views.py
from django.shortcuts import render

def home(request):
    return render(request, "relationship_app/home.html")
# -------------------------------
# Function-based view
# -------------------------------
def list_books(request):
    books = Book.objects.all()
    # Explicit template path
    return render(request, "relationship_app/list_books.html", {"books": books})

# -------------------------------
# Class-based view
# -------------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in right after registration
            return redirect("list_books")  # redirect to any page, e.g., book list
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

# --- Helpers for role checks ---
# relationship_app/views.py

def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

def is_admin(user):
    return hasattr(user, "profile") and user.profile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "profile") and user.profile.role == "Librarian"

def is_member(user):
    return hasattr(user, "profile") and user.profile.role == "Member"


# --- Role-based views ---
@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, "relationship_app/member_view.html")