from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^1/$', views.index1, name='index1'),
    url(r'^2/$', views.index2, name='index2'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^to_db/$', views.to_db, name='to_db'),
]
