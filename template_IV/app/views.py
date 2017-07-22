from django.shortcuts import render

def index(req):
    title = "Homepage"
    return render(req, 'blog/index.html', {'title': title})

def columns(req):
    title = "Columns"
    return render(req, 'blog/columns.html', {'title': title})

def login(req):
    title = "Login"
    return render(req, 'blog/login.html', {'title': title})
