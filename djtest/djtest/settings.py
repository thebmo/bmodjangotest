"""
Django settings for djtest project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# sqlite3 demo
# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
# }
# # Local Db
# DATABASES = {
    # 'default': {
        # 'ENGINE':'django.db.backends.mysql',
        # 'NAME': 'djnes_local',
        # 'USER': 'root',
        # 'PASSWORD': 'qazwert$0369',
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
    # }
# }
#import os
#virtenv = os.environ['PYTHONPATH'] + '../env/'
#virtualenv = os.path.join(virtenv, 'Scripts/activate_this.py')
#try:
#    execfile(virtualenv, dict(__file__=virtualenv))
#except IOError:
#    pass

# Live Db (clearDB)
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'bmodjanones',
        'USER': 'bc9b2ef1c7ad8f',
        'PASSWORD': '63fb3fce',
        'HOST': 'us-cdbr-azure-east-c.cloudapp.net',
        'PORT': '3306',
    }
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x!xs)g=z&a9i*vg_^n=a9955=pzd#hpbjfqz17e-6v9k#l5a%6'

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
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nes',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djtest.urls'

WSGI_APPLICATION = 'djtest.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

