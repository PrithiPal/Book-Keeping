# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class Author(models.Model) :

    author_auth = models.OneToOneField(User,primary_key=True)
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    country = models.CharField(max_length=100,default="Canada")
    username = models.CharField(max_length=100,null=False,unique=True)
    password = models.CharField(max_length=100,null=False)

    def __str__(self) :
        writer_full_name = str(self.first_name) + " " + str(self.last_name)
        return writer_full_name

    def clean_last_name(self) :
        print("CLEAN LAST NAME STARTS..")
        f_name = self.first_name
        l_name = self.last_name

        all_auth_names = [(str(x.first_name),str(x.last_name)) for x in self.objects.all()]
        if (f_name,l_name) in all_auth_names : # Entry with same first and last names already exists
            raise ValidationError(_("These two names already exists"))
        else :
            return l_name
            print("LAST NAME IS ",str(l_name))


class Book(models.Model) :

    title = models.CharField(max_length=100,null=False)
    author = models.ManyToManyField(Author,related_name='books')


    def __str__(self) :
        return self.title

class Country(models.Model) :

    country_code = models.CharField(max_length=2,null=False,default='')
    country_name = models.CharField(max_length=100,null=False,default='')


    def __str__(self) :
        return self.country_name
