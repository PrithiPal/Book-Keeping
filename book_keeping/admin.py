# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Author

@admin.register(Author)
class MyAdmin(admin.ModelAdmin) :
    pass

# Register your models here.
