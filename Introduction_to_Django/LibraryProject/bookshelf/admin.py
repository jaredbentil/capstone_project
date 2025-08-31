from django.contrib import admin

# Register your models here.

from .models import Book

# Register the Book model
admin.site.register(Book)

# Customize the admin interface for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    list_filter = ('author', 'publication_year')            # Filter options
    search_fields = ('title', 'author')                     # Search bar fields

# Register the Book model with the custom admin
admin.site.register(Book, BookAdmin)