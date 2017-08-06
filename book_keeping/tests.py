# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase,Client
from book_keeping.models import Author
from book_keeping.forms import SampleForm

class ValidationTests(TestCase) :
    def test_sampleform(self) :
        f_name = 'jugnu'
        l_name = 'jugnu'
        data = {'first_name':f_name,'last_name':l_name}
        f = SampleForm(data)
        resp = f.errors
        self.assertEqual(resp,None)
