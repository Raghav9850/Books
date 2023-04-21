from django import forms
from .models import Book, Author, Category


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['auth_name', 'email']
        widgets = {
            'auth_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'book_description', 'author', 'categories']
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'book_description': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'author': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'categories': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['categories'].required = False


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']
        widgets = {
            'cat_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }
