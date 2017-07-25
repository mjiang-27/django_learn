from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return render(req, 'home.html')

# Method used for the url format 'add/?a=4&b=5'
def add(req):
    a = req.GET['value_a']
    b = req.GET['value_b']
    c = int(a) + int(b)

    return HttpResponse(str(c))
