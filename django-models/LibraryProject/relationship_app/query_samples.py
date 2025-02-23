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
