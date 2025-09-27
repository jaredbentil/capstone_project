from django.db import models

# Create your models here.
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

#Define the Book Model
class Book(models.Model):

    title = models.CharField(max_length=200, help_text="The title of the book.")
    publication_year = models.IntegerField(help_text="The year the book was published.")
  
    # books from an Author 
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books', 
        help_text="The author of this book."
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
