# query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}:")
for book in books_by_author:
    print(f"- {book.title}")

# 2. List all books in a library
library = Library.objects.get(name="Main City Library")
books_in_library = library.books.all()
print(f"Books in {library.name}:")
for book in books_in_library:
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"The librarian for {library.name} is {librarian.name}")
