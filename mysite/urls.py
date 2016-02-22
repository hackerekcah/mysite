"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from polls import views

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^info/',include('info.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^application/',include('application.urls')),
    url(r'^accounts/', include('register.urls')),
    url(r'^showMeta/$', views.display_meta),
    url(r'^books/', include('books.urls')),
    url(r'^contact/',include('contact.urls')),
]
