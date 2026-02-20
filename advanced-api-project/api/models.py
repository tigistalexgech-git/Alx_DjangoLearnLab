from django.db import models

class Author(models.Model):
    """
    Author model represents a writer who can have multiple books.
    One-to-many relationship: One Author → Many Books
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model stores information about books written by an author.
    Each book is linked to one Author using a ForeignKey.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title