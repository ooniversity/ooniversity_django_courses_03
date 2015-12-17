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
SECRET_KEY = '*woucf0gphlf@tq=l7e_@0t42@s5p9s2=1!&r6w)!cj$cvea0l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


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
    'debug_toolbar',
    'django_extensions'
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

TIME_ZONE = 'UTC'

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

ADMINS = (('alex', 'ud3p@mail.ru'), ('alex', 'ex@gmail.ru'))

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#     }
# }

LOGGING = {
    'version': 1,
    'loggers':
    {
        'courses': {
            'handlers': ['courses_message'],
            'level': 'DEBUG',
        },
        'students': {
            'handlers': ['students_message'],
            'level': 'WARNING',
        }
    },
    'handlers':
    {
        'courses_message': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
            'formatter': 'course_format'
        },
        'students_message': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'students_logger.log'),
            'formatter': 'student_format'
        },
    },
    'formatters': {
        "course_format":{
            'format': '%(levelname)s %(message)s'
        },
        "student_format": {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },

    },
}

# try:
#     from local_settings import *
# except ImportError:
#     print 'Warning! local_settings are not defined!'
