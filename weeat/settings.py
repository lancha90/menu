"""
Django settings for weeat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FOLDER_PROJECT = os.path.dirname(os.path.realpath(__file__))

ADMINS = (
    ('Diego Mauricio Herrera Alzate', 'diegomao627@gmail.com'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xt#e2qw%o(ve%ys#uc5x06@j1#!od0e#=)=d=pkc6e5c7+s!l*'

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
    'rest_framework',
    'corsheaders',
    'api',
    'server',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'weeat.urls'
WSGI_APPLICATION = 'weeat.wsgi.application'

# ================= CORS CONFIGURATION ===================
USE_ETAGS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/v1/.*$'
# ================= END CORS CONFIGURATION ===================



# ================== S3 CONFIGURATION =========================

DEFAULT_FILE_STORAGE = 'server.s3utils.MediaS3BotoStorage' 
STATICFILES_STORAGE = 'server.s3utils.StaticS3BotoStorage'

AWS_ACCESS_KEY_ID = 'AKIAJ6NDBSYF5YSLO7YQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'weeat'

S3_URL = 'http://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_DIRECTORY = '/static/'
MEDIA_DIRECTORY = '/media/'
STATIC_URL = S3_URL + STATIC_DIRECTORY
MEDIA_URL = S3_URL + MEDIA_DIRECTORY

# ================== END S3 CONFIGURATION =========================

# =========== HEROKU CONFIGURATION =====================
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dacg9e30411ue',                      # Or path to database file if using sqlite3.
        'USER': 'bdkhufgevkawys',                      # Not used with sqlite3.
        'PASSWORD': 'Y9x6yM9odu1oz4-LBLBdCxhMQk',                  # Not used with sqlite3.
        'HOST': 'ec2-54-204-36-244.compute-1.amazonaws.com',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
STATIC_ROOT = 'staticfiles'
# =========== END HEROKU CONFIGURATION =====================


"""
# =========== LOCAL CONFIGURATION =====================
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'weeat',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '123456',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}
ALLOWED_HOSTS = []
STATIC_ROOT = ''

# =========== END LOCAL CONFIGURATION =====================
"""

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'America/Bogota'

LANGUAGE_CODE = 'es-CO'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(FOLDER_PROJECT,'static/css/image')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(FOLDER_PROJECT,'static'),
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(FOLDER_PROJECT,'html'),
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAuthenticated',
        #'django.contrib.auth',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
    ),
}
