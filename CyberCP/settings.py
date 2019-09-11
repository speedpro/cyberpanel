"""
Django settings for CyberCP project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xr%j*p!*$0d%(-(e%@-*hyoz4$f%y77coq0u)6pwmjg4)q&19f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'baseTemplate',
    'loginSystem',
    'packages',
    'websiteFunctions',
    'tuning',
    'serverStatus',
    'dns',
    'ftp',
    'userManagment',
    'databases',
    'mailServer',
    'serverLogs',
    'firewall',
    'backup',
    'managePHP',
    'manageSSL',
    'api',
    'filemanager',
    'manageServices',
    'pluginHolder',
    'emailPremium',
    'emailMarketing',
    'cloudAPI',
    'highAvailability',
    's3Backups',
    'dockerManager',
    'containerization',
    'CLManager'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'CyberCP.secMiddleware.secMiddleware'
]

ROOT_URLCONF = 'CyberCP.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CyberCP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cyberpanel',
        'USER': 'cyberpanel',
        'PASSWORD': 'Bz9gF7Hr7X4RtD',
        'HOST': '127.0.0.1',
        'PORT':'3307'
    },
    'rootdb': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER': 'root',
        'PASSWORD': 'sXm5VlRaAsXkDd',
        'HOST': 'localhost',
        'PORT': '',
    },
}

DATABASE_ROUTERS = ['backup.backupRouter.backupRouter']


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATIC_URL = '/static/'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('en', _('English')),
    ('cn', _('Chinese')),
    ('br', _('Bulgarian')),
    ('pt', _('Portuguese')),
    ('ja', _('Japanese')),
    ('bs', _('Bosnian')),
    ('gr', _('Greek')),
    ('ru', _('Russian')),
    ('tr', _('Turkish')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    ('pl', _('Polish')),
    ('vi', _('Vietnamese')),
    ('it', _('Italian')),
)

MEDIA_URL = '/home/cyberpanel/media/'
MEDIA_ROOT = MEDIA_URL