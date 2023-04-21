
from django.db import models

class Author(models.Model):
    auth_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.auth_name

class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.book_name
