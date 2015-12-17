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
SECRET_KEY = 'o)-ngq2-qshhu687cz2pa((@paj7x)j=734th0(pjf93v)$)y_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [ ]


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
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'th3fall3n0n3@yandex.ru'
EMAIL_HOST_PASSWORD = 'hamster12'
EMAIL_USE_SSL = True

ADMINS = (('Ivan', 'ivan.tarasenko@toatech.com'), ('Ne_Ivan', 'ivan.tarasenko@oracle.com') )

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

LOGGING = {
    'version': 1,
    'loggers': 
    {
	'courses': {
	    'handlers': ['courses_file'],
	    'level' : 'DEBUG'
	},
	'students': {
	    'handlers': ['students_file'],
	    'level': 'WARNING'
	}
    },
	'handlers':
    {
        'courses_file': {
	    'level': 'DEBUG',
	    'class': 'logging.FileHandler',
	    'filename': 'courses_logger',
	    'formatter': 'short'
	},
	'students_file': {
	    'level': 'WARNING',
	    'class': 'logging.FileHandler',
	    'filename': 'students_logger',
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
