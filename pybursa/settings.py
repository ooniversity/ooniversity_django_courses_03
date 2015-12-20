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
SECRET_KEY = '#(ry%ee*q_pqzoa9xf@a*vntmqqwdixb(rf9_h1@l1ex1ntn32'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['polygon.tk', '127.0.0.1']

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
    # 'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',  # for caches
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',  # for caches
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}


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

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder",
                       "django.contrib.staticfiles.finders.AppDirectoriesFinder"
                       )

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Email settings

# EMAIL_HOST = 'smtp-pulse.com'
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
#
# EMAIL_HOST_USER = 's.pod.pub@ya.ru'
# EMAIL_HOST_PASSWORD = 'ikm3tMPdoJtcp8'


EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'Sansiro'
EMAIL_HOST_PASSWORD = 't0iAO0OQhVmo0xHVr3pM'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SERVER_EMAIL = 's.pod.pub@ya.ru'
ADMINS = ('s.pod.pub@ya.ru',)

# Logging settings (added extensions)
# https://docs.djangoproject.com/en/1.7/topics/logging/#examples

LOGGING = {
    'version': 1,
    'loggers': {
        'courses': {
            'handlers': ['courses_log_file'],
            'level': 'DEBUG',
        },
        'students': {
            'handlers': ['students_log_file'],
            'level': 'WARNING',
        },
    },
    'handlers': {
        'courses_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
            'formatter': 'simple',
        },
        'students_log_file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'students_logger.log'),
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
    },
}

'''
DEBUG_TOOLBAR_PATCH_SETTINGS = False


def show_toolbar(request):
    return True
SHOW_TOOLBAR_CALLBACK = show_toolbar

INTERNAL_IPS = ('127.0.0.1', '162.211.227.228',)
'''