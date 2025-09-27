from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# --------------------------
# Custom User Manager
# --------------------------
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(username, email, password, **extra_fields)


# --------------------------
# Custom User Model
# --------------------------
class CustomUser(AbstractUser):
    """
    A custom user model with email as a unique identifier.
    """
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


# --------------------------
# User Profile (linked to CustomUser)
# --------------------------
class UserProfile(models.Model):
    """
    A one-to-one user profile linked to the custom user model.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


# --------------------------
# Library, Book, and Through Models
# --------------------------
class Author(models.Model):
    """
    Represents an author of a book.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book with a title, author, and publication year.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Library(models.Model):
    """
    Represents a library that can hold many books.
    """
    name = models.CharField(max_length=100)
    books = models.ManyToManyField("Book", through="Library_books")

    def __str__(self):
        return self.name


class Library_books(models.Model):
    """
    A through model for the ManyToMany relationship between Library and Book.
    """
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} in {self.library.name}"


class Librarian(models.Model):
    """
    Represents a librarian, with a one-to-one relationship to a Library.
    """
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name

class Member(models.Model):
    """
    Represents a library member who can belong to many libraries.
    """
    name = models.CharField(max_length=100)
    libraries = models.ManyToManyField(Library, related_name="members")

    def __str__(self):
        return self.name
