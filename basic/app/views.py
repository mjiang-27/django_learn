#coding:utf-8
from django.http import HttpResponse

def index(req):
    return HttpResponse(u"Welcom to mySite!");
