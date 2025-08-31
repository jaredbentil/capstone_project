# Create Operation
from bookshelf.models import Book

# Create a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Verify creation
print(Book.objects.all())

<QuerySet [<Book: 1984 by George Orwell (1949)>]>

---

# Retrieve Operation

from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

1984 George Orwell 1949


---

# Update Operation

from bookshelf.models import Book

# Update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
book = Book.objects.get(id=book.id)
print(book.title, book.author, book.publication_year)

Nineteen Eighty-Four George Orwell 1949

---


---

# Delete Operation

from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())

<QuerySet []>


