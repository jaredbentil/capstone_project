from rest_framework import serializers
from api.models import Author, Book
from django.utils import timezone

# Step 4: Create BookSerializer
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model. 
    It includes custom validation to ensure the publication year is not in the future.
    """
    
    class Meta:
        model = Book
        # Serialize all model fields for the Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Step 4: Custom Validation
    def validate_publication_year(self, value):
        """
        Custom validation method to check if the publication_year is in the future.
        If it is, a ValidationError is raised, preventing serialization.
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. The current year is {current_year}."
            )
        return value

# Step 4: Create AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):

    # Nested Serializer: This field uses the BookSerializer to represent 
    # the Author's related books (via the 'books' related_name).
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        # The fields include the simple 'name' and the complex, nested 'books' list.
        fields = ['id', 'name', 'books']



