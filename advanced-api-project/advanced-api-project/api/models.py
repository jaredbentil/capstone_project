from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
  
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    # The 'related_name' attribute allows us to access an author's books
    # from an author instance, e.g., author.books.all()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    
