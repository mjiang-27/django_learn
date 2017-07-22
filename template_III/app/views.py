from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    title = "Welcome to my django curriculum !!!"
    tutoriaList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info = {'site': 'mjiang', 'content': 'IT technologies'}
    return render(req, 'home.html', {'title': title, 'tutoriaList': tutoriaList, 'info': info})

def add(req, a, b):
    return HttpResponse(str(int(a) + int(b)))
