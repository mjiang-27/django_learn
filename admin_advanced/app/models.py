# -*- coding: utf-8 -*-

'''
modules used to make codes compatible for Python2.x and Python3.x
'''
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
# @python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()

    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(null=True, auto_now=True)

    '''
    Show the name of article in web for Python2.x
    def __unicode__(self):
        return self.title
    '''

    '''
    Show the name of article in web for Python3.x
    '''
    def __str__(self):
        return self.title

'''
Class used to show none-Fields in django admin page
'''
# @python_2_unicode_compatible
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"

    full_name = property(my_property)
