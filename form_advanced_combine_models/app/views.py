# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Book
from .forms import BookForm

def index(req):
    return render(req, 'books/index.html')

def add(req):
    if req.method == "POST":
        form = BookForm(req.POST)

        if form.is_valid():
            book_name = form.cleaned_data['name']
            book_author = form.cleaned_data['author']
            book_price = (int)(form.cleaned_data['price'])
            book_description = form.cleaned_data['description']

            book = Book(name=book_name, author=book_author, price=book_price, description=book_description)
            Book.objects.get_or_create(name=book.name, author=book.author, price=book.price, description=book.description)

            return HttpResponseRedirect(reverse('add_result'), {'book': book})

    else:
        form = BookForm(None)

    return render(req, 'books/add.html', {'form': form})

def add_result(req):
    return render(req, 'books/add_result.html')

def lists(req):
    books = Book.objects.all()

    return render(req, 'books/list.html', {'books': books})
