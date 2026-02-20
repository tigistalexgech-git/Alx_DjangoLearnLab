from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.test import override_settings
from .models import Book, Author


@override_settings(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',  # Separate test database
        }
    }
)
class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

       
        self.client.login(username='testuser', password='testpass123')

        # Create author & book
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2024,
            author=self.author
        )

    def test_get_books(self):
        url = reverse('book-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)   # ✅ response.data

    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2025,
            "author": self.author.id
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")  # ✅ response.data

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {
            "title": "Updated Book",
            "publication_year": 2023,
            "author": self.author.id
        }

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)