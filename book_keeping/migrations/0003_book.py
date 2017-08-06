# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-28 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_keeping', '0002_author_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.ManyToManyField(to='book_keeping.Author')),
            ],
        ),
    ]
