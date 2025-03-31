# serializers.py
from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested Author serializer

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']
