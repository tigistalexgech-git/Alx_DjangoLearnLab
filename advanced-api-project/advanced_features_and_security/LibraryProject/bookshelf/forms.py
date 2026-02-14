
from django import forms
from .models import Article
from .models import Book


class ExampleForm(forms.ModelForm):
    """
    ExampleForm is used to demonstrate secure form handling,
    CSRF protection, and input validation.
    """
    class Meta:
        model = Book
        fields = ['title', 'author']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
