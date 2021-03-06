#!/usr/bin/env python3

from setuptools import setup

with open('README.rst') as f:
	readme = f.read()

setup(
	name = "django-gitlab_auth",
	version = "0.1.1",
	description = "OpenID Connect authentication support for Django",
	long_description = readme,
	author = "Linus Lewandowski",
	author_email = "linus@lew21.net",
        url = "https://github.com/kkannan1982/django-auth-gitlab.git",
	keywords = "django,auth,oauth,openid,oidc,social,gitlab",
	license = "LGPLv2+",

    install_requires = ["django>=1.10.0"],

	packages = ["django_gitlab_auth"],
	package_data = {"": ["LICENSE"]},
	package_dir = {"django_gitlab_auth": "django_gitlab_auth"},
	zip_safe = True,
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: System Administrators',
		'Natural Language :: English',
		'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: System :: Systems Administration :: Authentication/Directory',
	]
)
