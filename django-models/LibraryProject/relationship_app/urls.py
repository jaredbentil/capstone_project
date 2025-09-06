
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("", RedirectView.as_view(pattern_name="list_books", permanent=False)),  # <--- NEW
    

    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    #path("admin-view/", views.admin_view, name="admin_view"),
    

    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
]
