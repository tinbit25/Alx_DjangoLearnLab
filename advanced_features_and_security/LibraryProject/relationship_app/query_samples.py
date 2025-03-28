from relationship_app.models import Library, Author, Book, Librarian

# Example: Retrieve a Library by name
library_name = "Central Library"  # Replace with an actual library name in your database
try:
    library = Library.objects.get(name=library_name)
    print(f"Library Found: {library}")
except Library.DoesNotExist:
    print("Library not found.")

# Example: Retrieve all books in the library
books_in_library = library.books.all() if library else []
print(f"Books in Library: {books_in_library}")

# Example: Retrieve the librarian managing this library
try:
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian: {librarian}")
except Librarian.DoesNotExist:
    print("No librarian assigned to this library.")

# ✅ Required: Retrieve an Author by name
author_name = "J.K. Rowling"  # Replace with an actual author name in your database
try:
    author = Author.objects.get(name=author_name)
    print(f"Author Found: {author}")
except Author.DoesNotExist:
    print("Author not found.")

# ✅ Required: Retrieve all books written by the author
books_by_author = Book.objects.filter(author=author) if 'author' in locals() else []
print(f"Books by {author_name}: {list(books_by_author)}")
