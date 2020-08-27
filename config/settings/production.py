from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['*.herokuapp.com']

DATABASES['default'] = dj_database_url.config()

WSGI_APPLICATION = 'config.wsgi.production.txt.application'

SITE_ID=1

django_heroku.settings(locals())