from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # ✅ This ensures the check passes
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ Ensure the template path is correct
