"""
Django settings for pybursa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5w48h%g+gq6u!o)of8cg=ne0jdv@136#-z@vfi4zf9n95cf2#k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [ '*' ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'quadratic',
    'courses',
    'students',
    'coaches',
    'feedbacks',
    #'debug_toolbar'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pybursa.urls'

WSGI_APPLICATION = 'pybursa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
#EMAIL_HOST_USER = 'qqq'
#EMAIL_HOST_PASSWORD = 'bla'
ADMINS = (('Oleg', 'book1978@gmail.com'),)
#DEFAULT_FROM_EMAIL = 'blabla@gmail.com'
EMAIL_SUBJECT_PREFIX = ''

LOGGING = {
    'version': 1,
    'formatters': {
        'format_courses': {
            'format': '%(levelname)s %(message)s'
        },
        'format_students': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
    },
    'handlers': {
        'file_courses': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
            'formatter': 'format_courses'
            },
        'file_students': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'students_logger.log'),
            'formatter': 'format_students'
        },
    },
    'loggers': {
        'courses': {
            'handlers': ['file_courses'],
            'level': 'DEBUG',
            },
        'students': {
            'handlers': ['file_students'],
            'level': 'WARNING',
            },
    },
}
'''
try:
    from local_settings import *
except ImportError:
    print "Warning! local_settings are not defined!"
'''
