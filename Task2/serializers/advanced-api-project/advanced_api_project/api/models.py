from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Represents an author in the system. 
    This model serves as the 'one' side of the one-to-many relationship with Book.
    """
    name = models.CharField(max_length=100, help_text="The full name of the author.")

    def __str__(self):
        return self.name

# Step 3: Define the Book Model
class Book(models.Model):
    """
    Represents a book, linked to a single Author.
    This model serves as the 'many' side of the one-to-many relationship.
    """
    title = models.CharField(max_length=200, help_text="The title of the book.")
    publication_year = models.IntegerField(help_text="The year the book was published.")
    
    # Foreign Key linking Book to Author. The 'related_name' allows accessing 
    # books from an Author instance (e.g., author_instance.books.all()).
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books', 
        help_text="The author of this book."
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
