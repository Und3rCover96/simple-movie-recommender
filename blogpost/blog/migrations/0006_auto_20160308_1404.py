# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-08 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movie_name',
            field=models.CharField(max_length=100),
        ),
    ]