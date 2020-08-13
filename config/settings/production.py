from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['*.herokuapp.com']

WSGI_APPLICATION = 'config.wsgi.production.application'

# django_heroku.settings(locals())