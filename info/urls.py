from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^info_to_db/$', views.info_to_db, name='info_to_db'),
    url(r'^info_form/$', views.info_form, name='info_form'),
]
