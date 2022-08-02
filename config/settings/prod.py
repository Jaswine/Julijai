import django_on_heroku
from decouple import config

from config.settings.dev import SECRET_KEY

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
  'julijai-it-hub.herokuapp.com',
  'julijai.blog',
]

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
  'version':1,
  'disable_existing_loggers': False,
  'formatters': {
    'verbose': {
      'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
      'datefmt': "%d/%b/%Y %H:%M:%S"
    },
    'simple': {
      'format': '%(levelname)s %(message)s'
    },
  },
  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'loging.StreamHandler',
    },
  },
  'loggers': {
    'MYAPP': {
      'handlers': ['console'],
      'level': 'DEBUG',
    },
  }
}

django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']