from __future__ import unicode_literals

# Create your models here.
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
         return self.first_name + " " + self.last_name
