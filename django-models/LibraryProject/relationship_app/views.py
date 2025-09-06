from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library
from .models import Library



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
