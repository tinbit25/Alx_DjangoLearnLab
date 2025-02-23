from django.shortcuts import render
from django.views.generic.detail import DetailView  # ✅ Correct import for DetailView
from .models import Library  # ✅ Ensure both Library and Book are imported
from .models import Book
# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Correct template path
    context_object_name = "library"  # Ensures "library" is available in templates
