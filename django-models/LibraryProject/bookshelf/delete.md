### Delete Operation

**Command:**
```python
from bookshelf.models import Book  # Import the Book model

# Retrieve the book instance you want to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
book.delete()

# Confirm deletion by attempting to retrieve all books
print(Book.objects.all())  # Expected Output: QuerySet([]) - No books remaining
