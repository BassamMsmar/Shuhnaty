import os
from .local_settings import *


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['24.199.67.221', 'www.bassammsmar.com']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shuhnaty',
        'USER': 'db_user',
        'PASSWORD': 'Shuhnaty@100',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/var/www/static-root/'
MEDIA_ROOT = '/var/www/media-root/'
