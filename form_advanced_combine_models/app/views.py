# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Used for csrf_token
from django.template import RequestContext

# Import modules from models and forms define by ouselves
from .models import Book
from .forms import BookForm

def index(req):
    # ToDo: add user login logics here
    return render(req, 'books/index.html')

def add(req):
    req_ctx = RequestContext(req)

    if req.method == "POST":
        form = BookForm(req.POST)

        if form.is_valid():
            book_name = form.cleaned_data['name']
            book_author = form.cleaned_data['author']
            book_price = (int)(form.cleaned_data['price'])
            book_description = form.cleaned_data['description']

            book = Book(name=book_name, author=book_author, price=book_price, description=book_description)
            Book.objects.get_or_create(name=book.name, author=book.author, price=book.price, description=book.description)

            return HttpResponseRedirect(reverse('add_result'))

    else:
        form = BookForm(None)
        req_ctx.push({'form': form})

    return render(req, 'books/add.html', {'req_ctx': req_ctx})

def add_result(req):
    return render(req, 'books/add_result.html')

def getKwargs(data={}):
    kwargs = {}

    for k, v in data.items():
        if v is not None and v != u'':
            kwargs[k] = v

    return kwargs

def delete(req):
    req_ctx = RequestContext(req)

    if req.method == "POST":
        form = BookForm(req.POST)

        if form.is_valid():
            clean_data = form.cleaned_data
            kwargs = getKwargs(clean_data)

            try:

                del_books = Book.objects.filter(**kwargs)
                req_ctx.push({'del_books': del_books})

                # Delete selected books
                del_books.delete()

            except:
                pass

            finally:
                # ToDo: response diffeently according to the post data
                return HttpResponseRedirect(reverse('delete_result'), {'req_ctx': req_ctx})

    else:
       form = BookForm(None)
       req_ctx.push({'form': form})

    return render(req, 'books/delete.html', {'req_ctx': req_ctx})

def delete_result(req):
    return render(req, 'books/delete_result.html')

def lists(req):
    books = Book.objects.all()

    return render(req, 'books/list.html', {'books': books})
