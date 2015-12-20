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
SECRET_KEY = '3zti90-ee8m=o1&et^5cd(rnnamji4@onmn*d)ce)**nl54g1&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quadratic',
    'courses',
    'students',
    'coaches',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
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
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"), )




LOGGING = {
    'version': 1,
    'loggers': {
       'courses.views': {
          'handlers': ['courses.views.file'],
          'level':'DEBUG',
       },
       'students.views': {
          'handlers': ['students.views.file'],
          'level':'WARNING',
       },
    },

    'handlers':
    {
       'courses.views.file': {
          'level': 'DEBUG',
          'class': 'logging.FileHandler',
          'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
          'formatter': 'cources',
       },
       'students.views.file': {
          'level': 'WARNING',
          'class': 'logging.FileHandler',
          'filename': os.path.join(BASE_DIR, 'students_logger.log'),
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

try: 
    from local_settings import *
except ImportError:
    print 'Warning! local_settings are not defined!'

