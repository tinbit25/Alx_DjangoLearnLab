from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Adding Filtering, Searching, and Ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering options (users can filter by these fields)
    filterset_fields = ['title', 'author', 'publication_year']

    # Search functionality (users can search by title or author)
    search_fields = ['title', 'author']

    # Ordering options (users can order results by these fields)
    ordering_fields = ['title', 'publication_year']
