from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.contact),
    url(r'^thanks/$', views.thanks),
]
