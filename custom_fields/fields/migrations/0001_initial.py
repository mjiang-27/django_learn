# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-24 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labels', fields.fields.ListField()),
                ('content', fields.fields.CompressedTextField(default='', null=True)),
            ],
        ),
    ]
