from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        """Ensure the book title is at least 3 characters long."""
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
