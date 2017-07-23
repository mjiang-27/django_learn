from django.shortcuts import render

# Create your views here.
from app.models import Person

def sign_up(req):
    user, created = Person.objects.get_or_create(last_name = 'Jiang', first_name = 'Mingming', age = 26) 
    return render(req, 'persons/signup.html', {'user': user})
