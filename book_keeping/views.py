# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from book_keeping.forms import AuthorLoginForm,AuthorAddForm,SampleForm
from book_keeping.models import Author
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings

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
            new_author = Author(author_auth = new_author_user,first_name=form_first_name,last_name=form_last_name,country = form_country, username=form_username, password=form_password)
            new_author.save()




            return HttpResponse("<h1 align=\"center\"> AUTHOR ADDED <\/h1>")

        else :
                form = AuthorAddForm()
                return render(request,"book_keeping/html/author_signin.html",{'form' : form})


    else :
        form = AuthorAddForm()
        return render(request,"book_keeping/html/author_signup.html",{'form' : form})

def author_login(request) :

    if request.method == "POST" :
        form = AuthorLoginForm(request.POST)
        if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            author_user = authenticate(username=username,password=password)
            if author_user :
                login(request,author_user)
                author = Author.objects.get(author_auth = author_user)
                return render(request,"book_keeping/html/author_homepage.html",{'author' : author,'dateform' : SampleForm})
            else :# incorrect user or password
                form = AuthorLoginForm()
                return render(request,"book_keeping/html/author_login.html",{'form' : form})
        else :#invalid form
                form = AuthorLoginForm()
                return render(request,"book_keeping/html/author_login.html",{'form' : form})
    else :#get page
        form = AuthorLoginForm()
        return render(request,"book_keeping/html/author_login.html",{'form' : form})

@login_required(login_url="/author-login")
def home(request) :
    author = Author.objects.get(author_auth = request.user)

    return render(request,"book_keeping/html/author_homepage.html",{'author' : author,'dateform' : SampleForm})


def author_logout(request) :
    logout(request)
    return redirect('/')

def parse_sampleform(request) :

    if request.method == "POST" :
        form = SampleForm(request.POST)
        if form.is_valid() :
            print("inside is_valid")
            return HttpResponse("is_valid")
        else :
            err_m = messages.error(request,"Error")
            return HttpResponse(err_m)
            

    else : #GET
        print("get method for the SAMPLE FORM")
        return redirect("/")
