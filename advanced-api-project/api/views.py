from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Book
from .serializers import BookSerializer

# List all books (READ – public)
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.

    Permissions:
    - Allow read-only access to unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Retrieve a single book by ID (READ – public)
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book using its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Create a new book (CREATE – authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.

    Permissions:
    - Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]



# Update an existing book (UPDATE – authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.

    Permissions:
    - Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]



# Delete a book (DELETE – authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.

    Permissions:
    - Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

