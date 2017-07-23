from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    tag_line = models.TextField()

    def __unicode__(self): # __str__ on Python 3
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    head_line = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    rating = models.IntegerField()

    def __unicode__(self):
        return self.head_line
