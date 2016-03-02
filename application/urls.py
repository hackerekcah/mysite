from django.conf.urls import include,url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='application_index'),
    url(r'^procedure/$', views.procedure, name='application_procedure'),
    url(r'^contact_us/$', views.contact_us, name='application_contact_us'),
    url(r'^user_profile/$', views.user_profile, name='application_user_profile'),
    url(r'^apply_for_visa/$', views.apply_for_visa, name='application_apply_for_visa'),
    url(r'^application_status/$', views.application_status, name='application_status'),
    url(r'^user_profile/save_change/$', views.profile_change, name='application_profile_change'),
    url(r'^blank/$', views.blank, name='application_blank'),
    url(r'', include('application.auth_urls')),

    url(r'^test/$',views.test, name='test')

]