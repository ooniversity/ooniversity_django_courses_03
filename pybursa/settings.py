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
#SECRET_KEY = '9edy9tsm+2*0nfw-s(a*rfb71ra6ck71szy5b_m#yywp3k0a#q'
SECRET_KEY = '4_c)!ymup1nmcx28a0&-j7d$vekn9h0v)n=!^k*c7!@%g!nv2u'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'coaches',
    'courses',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'feedbacks',
    'polls',
    'quadratic',
    'students',
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

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

ADMINS = (("Vitalii", "golv1974@gmail.com"),)

DEFAULT_FROM_EMAIL = "test_python@gmail.com"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file1': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            #'filename': '/path/to/django/debug.log',
            'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
        },
        'file2': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            #'filename': '/path/to/django/debug.log',
            'filename': os.path.join(BASE_DIR, 'students_logger.log'),
        },
    },
    'loggers': {
        'courses.views': {
            'handlers': ['file1'],
            'level': 'DEBUG',
            #'level': 'INFO',
            'propagate': True,
        },
    },
    'loggers': {
        'students.views': {
            'handlers': ['file2'],
            'level': 'DEBUG',
            #'level': 'INFO',
            'propagate': True,
        },
    },
}

