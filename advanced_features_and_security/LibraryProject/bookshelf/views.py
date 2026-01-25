
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article
from django import forms
from .forms import ArticleForm
from .models import Book
from .forms import BookForm

@permission_required('bookshelf.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'bookshelf/article_list.html', {'articles': articles})

@permission_required('bookshelf.can_create', raise_exception=True)
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'bookshelf/article_form.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'bookshelf/article_form.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('article_list')
    return render(request, 'bookshelf/article_confirm_delete.html', {'article': article})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Displays a list of all books (or articles) that the user has permission to view.
    """
    books = Article.objects.all()  # Replace Article with Book if needed
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Secure list view using Django ORM (prevents SQL injection)
    """
    books = Book.objects.all()  # ORM auto-escapes SQL
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    Secure form handling with validation
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():   # Input validation
            form.save()
    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})