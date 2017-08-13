
from django import forms
from book_keeping.models import Author,Country,Book,Language
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .validations import validate_form_author_names_no1,validate_form_username_conventions_no2

class AuthorLoginForm(forms.Form) :

    username = forms.CharField(label="Username",widget=forms.TextInput())
    password = forms.CharField(label="Password",widget=forms.PasswordInput())



    # validations are located in authenticaion backend

class AuthorAddForm(forms.Form) :


    FORM_NAME = "AuthorAddForm"
    first_name = forms.CharField(label="FirstName")
    last_name = forms.CharField(label="LastName")
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    #username = forms.CharField(label="username",min_length=8,max_length=32,validators=[validate_form_username_conventions_no2,])
    username = forms.CharField(label="username",max_length=32)
    password = forms.CharField(widget=forms.PasswordInput(),max_length=32)


    # store country_name instead of Country class
    def clean_country(self) :

            country = self.cleaned_data['country']
            print("COUNTRY TYPE: ",type(country))
            return str(country.country_name) # origin format : u'' now format : '' (string)


    def clean(self) :
        data = super(AuthorAddForm,self).clean()
        # validations, they stores exceptions in self.errors
        validate_form_author_names_no1(data['first_name'],data['last_name'])



    def name(self) :
        return self.FORM_NAME



class AuthorAddBookModelForm(forms.ModelForm) :

    language = forms.ModelChoiceField(queryset=Language.objects.all())

    class Meta :
        model = Book
        fields = ['title','language',]
