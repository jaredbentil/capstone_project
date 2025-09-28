from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__' # Includes id, title, publication_year, and author

    def validate_publication_year(self, value):
     
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
 
    # This uses the 'related_name' from the Book model's ForeignKey
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        # We explicitly list the fields to include our custom nested 'books' field.
        fields = ['id', 'name', 'books']