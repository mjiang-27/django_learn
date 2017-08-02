from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
