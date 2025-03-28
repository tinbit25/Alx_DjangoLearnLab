from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Enable search by title and author
    search_fields = ('title', 'author')

    # Filters for publication year and author
    list_filter = ('publication_year', 'author')

# Register the Book model with custom admin options
admin.site.register(Book, BookAdmin)
