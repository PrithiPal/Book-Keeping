
from django import forms
from book_keeping.models import Author,Country
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
class AuthorLoginForm(forms.Form) :

    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())

    # validations

    def clean(self) :
        data = super(AuthorLoginForm,self).clean()
        if data['username'] not in [str(x.username) for x in User.objects.all()] :
            raise ValidationError(_("Username not exists"))






class AuthorAddForm(forms.Form) :

    first_name = forms.CharField(label="FirstName")
    last_name = forms.CharField(label="LastName")
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput())


    # store country_name instead of Country class
    def clean_country(self) :
        country = self.cleaned_data['country']
        return country.country_name




class SampleForm(forms.Form) :

    CHOICES = (
    ('A','Apple'),
    ('B','Babble'),
    ('C','City'),
    ('D','Delhi'),
    )

    add_author = forms.ModelMultipleChoiceField(queryset = Author.objects.all(),widget=forms.CheckboxSelectMultiple)
    add_author_2 = forms.ModelMultipleChoiceField(queryset = Author.objects.all(),widget=forms.CheckboxInput)
