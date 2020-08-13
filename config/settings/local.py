from .base import *

import json

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.local.application'


SECRETS = json.load(open(os.path.join(SECRET_DIR, 'base.json')))
SECRET_KEY = SECRETS['SECRET_KEY']