from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.contrib import auth
from django.contrib.auth.models import User

def sign_in(req):
    errors = []

    if req.method == "POST":
        data = req.POST
        name = data["username"]
        password = data["password"]
        user = auth.authenticate(username = username, password = password)

        if user:
            if user.is_active:
                auth.login(req, user)
                return HttpRedirect('account/index.html')
            else:
                errors.append("Disabled account.")
        else:
            errors.append("Invalid user")

    return render(req, 'signin.html', {"errors": errors})

def sign_up(req):
    errors = []

    if req.method == "POST":
        data = req.POST
        name = data['username']
        password = data["password"]
        password2 = data["password2"]
        email = data["email"]

        print "" + name + " " + password + " " + " " + password + " " + email

        if not name:
            errors.append("Please input account.")

        if not password:
            errors.append("Please input password")

        if not password2:
            errors.append("Please input password2")

        if password is not None and password2 is not None:
            if password == password2:
                compare_flag = True
            else:
                errors.append("Passwords input are not consistent.")

        if not email:
            errors.append("Please input email")

        if name is not None and password is not None and password2 is not None and email is not None and compare_flag:
            # ToDo: check whether user already exists
            user = User.objects.create_user(name, email, password)
            user.is_active = True
            user.save
            return HttpResponseRedirect('accounts/index.html')

    return render(req, 'signup.html', {'errors': errors})

def log_out(req):
    logout(req)
    return HttpResponseRedirect(reverse('home')) 

def home(req):
    return render(req, 'home.html')

def index(req):
    return render(req, 'accounts/index.html')
