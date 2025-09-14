# Update Operation

from bookshelf.models import Book

# Update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
book = Book.objects.get(id=book.id)
print(book.title, book.author, book.publication_year)

Expected Output:

Nineteen Eighty-Four George Orwell 1949