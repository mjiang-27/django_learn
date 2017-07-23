from django.shortcuts import render

from app.models import Blog, Author, Entry

# Create your views here.
def home(req):
    homepage="Welcome to your own blog !"

    return render(req, 'blog/home.html', {'homepage': homepage})

def load_blogs():
    blog1 = Blog()
    blog1.title = "Useage of basic model in django"
    blog1.tag_line = "This is tag line 1"
    blog1.save()

    blog2 = Blog()
    blog2.title = "Useage of advanced model in django"
    blog2.tag_line = "This is tag line 2"
    blog2.save()

    blogs = []
    blogs.append(blog1)
    blogs.append(blog2)

    return blogs

def show_blogs(req):
    blogs = load_blogs()
    return render(req, 'blog/blogs.html', {'blogs': blogs})

def load_authors():
    author1 = Author(name='qingfeng-27', email='JMM2015@163.com')
    author1.save()

    author2 = Author(name='mjiang', email='mjiang@163.com')
    author2.save()

    authors = []
    authors.append(author1)
    authors.append(author2)

    return authors

def show_authors(req):
    authors = load_authors()
    return render(req, 'blog/authors.html', {'authors': authors})
'''
def show_entries(req):
    entries = []
    return render(req, 'blog/entires.html', {'entries': entries})
'''
