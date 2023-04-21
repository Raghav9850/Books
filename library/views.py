
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, AuthorForm, CategoryForm


def list_books(request):
    books = Book.objects.all()
    return render(request, 'library/list_books.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})


def update_book(request, id):
    book = Book.objects.get(pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/update_book.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
    else:
        form = AuthorForm()
    return render(request, 'library/add_author.html', {'form': form})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
    else:
        form = CategoryForm()
    return render(request, 'library/add_category.html', {'form': form})
