

from django.conf.urls import url
from book_keeping import views

urlpatterns = [
url(r'^$',views.index,name="index"),
##url(r'^author-login$',views.author_login,name="author_login"),
url(r'author-signup',views.author_signup,name="author_signup"),
url(r'author-login',views.author_login,name="author_login"),
url(r'home',views.home, name="home"),
url(r'author-logout',views.author_logout,name="author_logout"),
url(r'sampleform',views.parse_sampleform,name="sampleform"),
]
