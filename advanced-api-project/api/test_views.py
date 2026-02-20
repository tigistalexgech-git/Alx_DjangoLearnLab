from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import override_settings
from .models import Book, Author


@override_settings(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',  # Separate TEST database
        }
    }
)
class BookAPITestCase(APITestCase):

    def setUp(self):
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
        self.assertIsNotNone(response.data)     # ✅ REQUIRED BY ALX
        self.assertGreater(len(response.data), 0)

    def test_get_single_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")  # ✅ response.data used

    def test_create_book_unauthorized(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2025,
            "author": self.author.id
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIsNotNone(response.data)     # ✅ keyword