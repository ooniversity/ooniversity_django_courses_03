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
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as DEFAULT_TEMPLATE_CONTEXT_PROCESSORS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e%9ylkrs0+fx7*qq8mc!$_ynq!tf=7v%k6jssa_b=$)#kdf%x%'

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
    'students',
    'courses',
    'coaches',
    'quadratic',
    'feedbacks'
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


TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
ADMINS = (('Me','d3nshapoval@gmail.com'),'Ups','dustydevol@ukr.net')


LOGGING = {
    'version': 1,
    'loggers': 
    {
    'courses': {
        'handlers': ['courses_logs'],
        'level' : 'DEBUG'
    },
    'students': {
        'handlers': ['students_logs'],
        'level': 'WARNING'
    }
    },
    'handlers':
    {
        'courses_logs': {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
        'formatter': 'short'
    },
    'students_logs': {
        'level': 'WARNING',
        'class': 'logging.FileHandler',
        'filename': os.path.join(BASE_DIR, 'students_logger.log'),
        'formatter': 'detail'
    }
    },
    'formatters': {
        'detail': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
        'short': {
            'format': '%(levelname)s %(message)s'
        },
    },
}