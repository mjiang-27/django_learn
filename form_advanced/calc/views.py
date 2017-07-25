# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Introduce classes in forms
from .forms import AddForm

def index(req):
    if req.method == "POST": # Post forms
        form = AddForm(req.POST) # Get data in post forms

        if form.is_valid(): # Validate data post
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else: # Access url as usual
        form = AddForm()
        return render(req, 'home.html', {'form': form})
