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
SECRET_KEY = 'aus&e=-0$sgg^@$a&3(5mfhu*=&#8n3iwu(p(8^)yup7@w-&&i'

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
    "django.contrib.staticfiles.finders",
    'polls',    
    'quadratic',
    'courses',
    'students',
    'coaches',
    'feedbacks',
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

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Variable for feedback 
# 
# 
# 
ADMINS = (('mutekey', 'kirillushkov@gmail.com'), ('another_one', 'kirillushkov@meta.ua') )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{ 
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'        },
    },
    'handlers': {
        'file_courses': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'courses_logger.log',
            'formatter' : 'simple'
        },
        'file_students': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'students_logger.log',
            'formatter' : 'verbose'
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