# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-14 01:09
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('book_keeping', '0020_auto_20170813_0538'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='author',
            managers=[
                ('genre', django.db.models.manager.Manager()),
            ],
        ),
    ]
