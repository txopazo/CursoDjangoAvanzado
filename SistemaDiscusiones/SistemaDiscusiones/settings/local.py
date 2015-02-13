from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER' : 'cursodjango',
        'PASSWORD' : 'pass',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}


STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '1045719785444394'
SOCIAL_AUTH_FACEBOOK_SECRET = '1637d7bfd47170461626f8c7390325a2'

SOCIAL_AUTH_TWITTER_KEY ='rpZvjHwhMSXyRIH4Tp4dpVBcB'
SOCIAL_AUTH_TWITTER_SECRET = 'Y7e5ZRnITOfvwYYH39LBtGRdazvlUWa546868PAxBQkPOZvgyn'
