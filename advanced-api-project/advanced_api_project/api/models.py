from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Model representing an Author.
    This model serves as the 'one' side in the one-to-many relationship 
    with the Book model.
    """
    name = models.CharField(max_length=200, help_text="The full name of the author.")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a Book.
    This model is on the 'many' side of the one-to-many relationship, 
    linked to an Author via a ForeignKey.
    """
    title = models.CharField(max_length=255, help_text="The title of the book.")
    publication_year = models.IntegerField(help_text="The year the book was published.")
    
    # ForeignKey creates the one-to-many relationship.
    # related_name='books' allows us to access all books for a specific 
    # author via author_instance.books.all().
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books',
        help_text="The author of this book."
    )

    class Meta:
        ordering = ['-publication_year', 'title']
        unique_together = ('title', 'author')

    def __str__(self):
        return f'"{self.title}" by {self.author.name}'
