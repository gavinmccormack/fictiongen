# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-10 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markov_functions', '0008_auto_20171018_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
