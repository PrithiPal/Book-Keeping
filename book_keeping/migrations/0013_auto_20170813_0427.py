# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-13 04:27
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('book_keeping', '0012_auto_20170807_2332'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('authors', django.db.models.manager.Manager()),
            ],
        ),
    ]
