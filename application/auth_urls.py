"""
URL patterns for the views included in ``django.contrib.auth``.

Including these URLs (via the ``include()`` directive) will set up the
following patterns based at whatever URL prefix they are included
under:

* User login at ``login/``.

* User logout at ``logout/``.

* The two-step password change at ``password/change/`` and
  ``password/change/done/``.

* The four-step password reset at ``password/reset/``,
  ``password/reset/confirm/``, ``password/reset/complete/`` and
  ``password/reset/done/``.

The URLconfs in the built-in registration workflows already have an
``include()`` for these URLs, so if you're using one of them it is not
necessary to manually include these views.

"""

from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'application/login.html'},
        name='application_login'),

    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'application/index.html'},
        name='application_logout'),

    url(r'^password/change/$',
        auth_views.password_change,
        {'post_change_redirect': 'application_password_change_form',
         'template_name':'application/password_change_form.html'},
        name='application_password_change_form'),

    url(r'^password/reset/$',
        auth_views.password_reset,
        {'template_name': 'application/password_reset.html',
            'post_reset_redirect': 'application_password_reset_done',
            'email_template_name': 'application/password_reset_email.txt'},
        name='application_password_reset'),

    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name':'application/password_reset_confirm.html',
            'post_reset_redirect': 'application_password_reset_complete'},
        name='application_password_reset_confirm'),

    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        {'template_name':'application/password_reset_complete.html'},
        name='application_password_reset_complete'),

    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        {'template_name':'application/password_reset_done.html'},
        name='application_password_reset_done'),
]
