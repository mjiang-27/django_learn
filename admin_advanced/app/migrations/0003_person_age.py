# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-25 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
    ]