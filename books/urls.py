from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^search-form/$', views.search_form),
    url(r'^search-form/search/$', views.search),
]
