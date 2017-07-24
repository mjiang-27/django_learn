from __future__ import unicode_literals

from django.db import models

from .fields import ListField, CompressedTextField

# Create your models here.
class Article(models.Model):
    labels = ListField()
    content = CompressedTextField(null=True, default='')
