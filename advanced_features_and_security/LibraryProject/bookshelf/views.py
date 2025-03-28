# views.py

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# List of books with permission check
@permission_required('books.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'book_list.html', {'books': books})
