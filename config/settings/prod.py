import django_on_heroku
from decouple import config

from config.settings.dev import SECRET_KEY

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
  'zackp-basic-blog.herokuapp.com',
  'zackp.blog',
]