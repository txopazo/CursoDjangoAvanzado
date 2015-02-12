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

SOCIAL_AUTH_FACEBOOK_KEY = '1461568030778452'
SOCIAL_AUTH_FACEBOOK_SECRET = 'a94f50d04acd13958e7b849517851cfd'

SOCIAL_AUTH_TWITTER_KEY ='rpZvjHwhMSXyRIH4Tp4dpVBcB'
SOCIAL_AUTH_TWITTER_SECRET = 'Y7e5ZRnITOfvwYYH39LBtGRdazvlUWa546868PAxBQkPOZvgyn'
