from django.shortcuts import render
from django.http import HttpResponse

# utils imported for redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

def old_add2_redirect(req, a, b):
    return HttpResponseRedirect(reverse('add2', args=(a, b))) 

def index(req):
    return render(req, 'home.html')

# Method used for the url format 'add/?a=4&b=5'
def add(req):
    a = req.GET['a']
    b = req.GET['b']
    c = int(a) + int(b)

    return HttpResponse(str(c))

# Method used for the format 'add/a/b' 
def add2(req, a, b):
    c = int(a) + int(b)
    
    return HttpResponse(str(c))
