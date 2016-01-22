from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    #url(r'^submit/$', views.submit, name='submit'),
    url(r'^to_db/$', views.to_db, name='to_db'),
    url(r'^test/$', views.test, name='test'),
    url(r'^validate/$', views.validate, name='validate'),
]
