# -*- coding: utf-8 -*-

from django.forms import ModelForm

from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'price', 'description']
