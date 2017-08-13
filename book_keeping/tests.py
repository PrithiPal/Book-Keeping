# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase,Client
from book_keeping.models import Author,Country
from book_keeping.forms import AuthorAddForm

class ValidationTests(TestCase) :

    # TESTS VALIDATION THAT FIRST AND LAST NAME TOGETHER CAN'T BE SAME
    def test_validation_no1(self) :
        FIRST_NAME = "my_name_is_king"
        LAST_NAME = "my_name_is_king"

        data = {'first_name':str(FIRST_NAME),'last_name':str(LAST_NAME),'country' : 'India','username':'pencilpencil','password':'pencil'}
        f = AuthorAddForm(data)
        #print(f.errors.as_data())
        self.assertFalse(f.errors.has_key('__all__'))

    # TESTS VALIDATION THAT USERNAME SHOULD SATISFY DEFINED REGEX.
    def test_validation_no2(self) :

        ILLEGAL_USERNAME = "++"
        data = {'username': str(ILLEGAL_USERNAME), 'country': Country.objects.all() , 'first_name': 'bb', 'last_name': 'singh', 'password': 'f'}
        f = AuthorAddForm(data)
        #print(f.errors.as_data())
        self.assertTrue(f.errors.has_key('username'))
