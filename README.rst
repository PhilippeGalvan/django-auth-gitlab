Django-GitLab-Auth - GitLab authentication support for Django
=============================================================

This is a Django login view that authenticates against GitLab.

Use it if you own a single GitLab instance that you want to use as
a OAuth Authentication Server between multiple apps.

See also django-auth-oidc_.

Requirements
------------

- Python 3.6+. **Python 2 is not supported, and won’t ever get supported.**
- Django 1.10+

Installation
------------

.. code:: python

    pip install django-gitlab-auth

settings.py
~~~~~~~~~~~

.. code:: python

    INSTALLED_APPS += ['django_gitlab_auth']

urls.py
~~~~~~~

.. code:: python

    urlpatterns += [
        url(r'^accounts/login/', include('django_gitlab_auth.urls')),
    ]

Configuration
-------------

GitLab
~~~~~~

App's redirect URI: http(s)://app-domain/accounts/login/callback

App's environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* GITLAB_SERVER - Gitlab Server URL - with trailing slash.
* GITLAB_CLIENT_ID - Client ID received from GitLab
* GITLAB_CLIENT_SECRET - Client secret received from GitLab

.. _django-auth-oidc: https://github.com/LEW21/django-auth-oidc
