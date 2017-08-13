# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from book_keeping.forms import AuthorLoginForm,AuthorAddForm,AuthorAddBookModelForm
from book_keeping.models import Author,Book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views import View
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from django.contrib import messages



def index(request) :
    return render(request,'book_keeping/html/index.html',{})


def author_signup(request) :

    if request.method == "POST" :
        form = AuthorAddForm(request.POST)

        if form.is_valid() :

            form_first_name = form.cleaned_data['first_name']
            form_last_name = form.cleaned_data['last_name']
            form_country = form.cleaned_data['country']
            form_username = form.cleaned_data['username']
            form_password = form.cleaned_data['password']

            # User
            new_author_user = User.objects.create_user(username=form_username,password=form_password)
            new_author_user.save()
            new_author_user.is_active = True

            #Author
            new_author = Author(author_auth = new_author_user,first_name=form_first_name,last_name=form_last_name,country = form_country)
            new_author.save()

            return HttpResponse("<h1 align=\"center\"> AUTHOR ADDED <\/h1>")

        else : # FORM IS NOT VALID
                print("------------ INVALID FORM ------------")
                print("ERROS : ",form.errors)
                form = AuthorAddForm()
                return render(request,"book_keeping/html/author_signup.html",{'form' : form})


    else : # GET FORM REQUEST

        form = AuthorAddForm()
        print("------------  GET REQUEST ------------")
        return render(request,"book_keeping/html/author_signup.html",{'form' : form})

def author_login(request) :

    if request.method == "POST" :
        form = AuthorLoginForm(request.POST)
        if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            author_user = authenticate(username=username,password=password)
            if author_user :
                # bug : allowes superuser but can't find author entry (not created for superuser), so thrown exception.
                login(request,author_user)
                author = Author.objects.get(author_auth = author_user) # load data for author_user
                return redirect('/home')
            else :# incorrect user or password
                form = AuthorLoginForm()
                return render(request,"book_keeping/html/author_login.html",{'form' : form})
        else :#invalid form
                form = AuthorLoginForm()
                return render(request,"book_keeping/html/author_login.html",{'form' : form})
    else :#get page
        print("------GET FORM ---------")
        form = AuthorLoginForm()
        return render(request,"book_keeping/html/author_login.html",{'form' : form})


# Author's Homepage View
@login_required(login_url="/author-login")
def home(request) :
    author = Author.objects.get(author_auth = request.user)

    return render(request,"book_keeping/html/author_homepage.html",{'author' : author})


class AuthorAddBookView(CreateView) :

    form_class = AuthorAddBookModelForm
    template_name = "book_keeping/html/author_add_book.html"
    success_url = '/home'

    def form_valid(self,form) :

        title = form.cleaned_data['title']
        author = form.cleaned_data['author']
        language = form.cleaned_data['language']


        # saving
        NewBook = Book(title=title,language=language)
        NewBook.save()
        NewBook.author.add(author)
        NewBook.save()
        #form.savem2m()
        messages.add_message(self.request,messages.INFO,'Book Successfully Added')

        return redirect(self.success_url)


# login not necessarily required
class BookListView(ListView) :
    model = Book
    template_name = "book_keeping/html/author_books_list.html"
    context_object_name = "book"

    def get_queryset(self) :

        person = self.kwargs['person']
        if str(person) == "all" :
            return Book.objects.all()
        elif str(person) == "my" :

            if self.request.user.is_authenticated : # Author user logedin

                user_author = Author.objects.get(author_auth__exact=self.request.user)
                return Book.objects.filter(author__exact=user_author)
            else :
                # add message here that you're not logged in
                return redirect("/")

# Author's Logout
def author_logout(request) :
    logout(request)
    return redirect('/')


class SampleView(View) :
    def get(self,request) :
        return render(request,"book_keeping/html/sample.html",{})
