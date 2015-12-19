"""
Django settings for project project.

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
SECRET_KEY = 'fa-qrmpyaa#=ffc*1(a^k3k**17eyy$=3#84ev0&2pd*uwzdru'

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
    'courses',
    'students',
    'coaches',
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

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder", "django.contrib.staticfiles.finders.AppDirectoriesFinder")
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'templates','courses'), os.path.join(BASE_DIR, 'templates', 'students'), os.path.join(BASE_DIR, 'quadratic', 'templates'))
ADMINS = (('ostrenko', 'ostrenko@yandex.ru'),('gmail','mr.ostrenko@gmail.com'))
EMAIL_HOST = 'mail.hzmk.com.ua'
EMAIL_PORT = '26'
EMAIL_HOST_USER = 'ostrenko@hzmk.com.ua'
EMAIL_HOST_PASSWORD = 'Q69DjekF'

try:
    from local_settings import *
except ImportError:
    print "Warning! Error importing local_settings.py"

LOGGING = {
    'version': 1,
    'handlers': {
        'file_courses': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
        },
        'file_students': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'students_logger.log'),
        },
    },
    'loggers': {
        'courses': {
            'handlers': ['file_courses'],
            'level': 'DEBUG',
            'propagate': True,
            'formatter': 'courses',
        },
        'students': {
            'handlers': ['file_students'],
            'level': 'WARNING',
            'propagate': True,
            'formatter': 'students',
        },

    },

    'formatters': {
        'cources': {
            'format': '%(levelname)s %(message)s'
        },
        'students': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
    },
}
