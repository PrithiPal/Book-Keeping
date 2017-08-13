

from django.conf.urls import url
from book_keeping import views
from book_keeping.models import Book



urlpatterns = [
url(r'^$',views.index,name="index"),
##url(r'^author-login$',views.author_login,name="author_login"),
url(r'author-signup',views.author_signup,name="author_signup"),
url(r'author-login',views.author_login,name="author_login"),
url(r'home',views.home, name="home"),
url(r'author-logout',views.author_logout,name="author_logout"),
url(r'^add-book$',views.AuthorAddBookView.as_view(),name="add_book"),
url(r'^books-(?P<person>all|my)$',views.BookListView.as_view(),name="books"),
url(r'^sample$',views.SampleView.as_view(),name="sample"),
]
