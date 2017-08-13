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


    def __str__(self) :
        writer_full_name = str(self.first_name) + " " + str(self.last_name)
        return writer_full_name

    def all(self) :
        return (self.author_auth,str(self.first_name),str(self.last_name),str(self.country))


class Language(models.Model) :
    name = models.CharField(max_length=49,null=True)
    lang_code = models.CharField(max_length=2,null=True)

    def __str__(self) :
        return self.name

class Genre(models.Model) :
    GENRE_TYPE_CHOICES = (
    ('Fiction',"Fictional Work"),
    ('Non-Fiction',"Non-Fictional Work"),
    )
    name = models.CharField(max_length=10,null=True)
    genre_type = models.CharField(choices=GENRE_TYPE_CHOICES,null=True,max_length=20)

    def __str__(self) :
        return self.name


class Book(models.Model) :

    title = models.CharField(max_length=100,null=False)
    author = models.ManyToManyField(Author,related_name='books')
    language = models.ForeignKey(Language,on_delete=models.SET_DEFAULT,default=1 )# default is English langauge
    genre = models.ForeignKey(Genre,on_delete=models.SET_DEFAULT,default=1)

    def __str__(self) :
        return self.title

class Country(models.Model) :

    country_code = models.CharField(max_length=2,null=False,default='')
    country_name = models.CharField(max_length=100,null=False,default='')


    def __str__(self) :
        return self.country_name
