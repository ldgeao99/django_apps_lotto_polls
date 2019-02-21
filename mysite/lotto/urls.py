"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lotto import views

urlpatterns = [
    url(r'^admin/', admin.site.urls), #localhost:8000/admin일 때
    url(r'^$', views.index),          #localhost:8000/일 때 views.index에 연결해준다.
    url(r'^lotto/$', views.index2, name='index'),
    url(r'^lotto/new/$', views.post, name='new_lotto'),
    #url(r'^lotto/[0-9]+/detail/$', views.detail1, name='detail1'), #regular expression 사용, localhost:8000/555/detail 같은 링크연결이 가능

    #localhost:8000/555/detail 같은 링크연결이지만 사용자가 링크 클릭시 눌린 객체의 primary key가 url에 자동으로 들어감
    url(r'^lotto/(?P<lottokey>[0-9]+)/detail/$', views.detail, name='detail'),
]
