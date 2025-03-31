from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        """Set up test data and client"""
        self.client = APIClient()
        
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)  # Authenticate client

        # Create sample books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2022)

        self.valid_book_data = {"title": "New Book", "author": "New Author", "publication_year": 2023}
        self.update_book_data = {"title": "Updated Book", "author": "Updated Author", "publication_year": 2024}

    def test_list_books(self):
        """Test retrieving the list of books"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)  # Expecting 2 books

    def test_retrieve_book(self):
        """Test retrieving a single book"""
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], self.book1.title)

    def test_create_book(self):
        """Test creating a new book"""
        response = self.client.post("/api/books/create/", self.valid_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        """Test updating an existing book"""
        response = self.client.put(f"/api/books/update/{self.book1.id}/", self.update_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(f"/api/books/delete/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """Test filtering books by author"""
        response = self.client.get("/api/books/?author=Author A")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_search_books(self):
        """Test searching for a book by title"""
        response = self.client.get("/api/books/?search=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_order_books(self):
        """Test ordering books by publication_year"""
        response = self.client.get("/api/books/?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]["title"], "Book One")

    def test_unauthenticated_access(self):
        """Test that unauthenticated users cannot create, update, or delete books"""
        self.client.force_authenticate(user=None)  # Logout user
        
        create_response = self.client.post("/api/books/create/", self.valid_book_data, format="json")
        self.assertEqual(create_response.status_code, status.HTTP_401_UNAUTHORIZED)

        update_response = self.client.put(f"/api/books/update/{self.book1.id}/", self.update_book_data, format="json")
        self.assertEqual(update_response.status_code, status.HTTP_401_UNAUTHORIZED)

        delete_response = self.client.delete(f"/api/books/delete/{self.book1.id}/")
        self.assertEqual(delete_response.status_code, status.HTTP_401_UNAUTHORIZED)
