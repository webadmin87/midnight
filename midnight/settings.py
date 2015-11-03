"""
Django settings for midnight project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%6fqr9$#ab!pwrw7yamrktl87e^@bc=fmujwr08s^o^led5^8j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    'redactor',
    'sorl.thumbnail',
    'bootstrap_pagination',
    'django_assets',
    'bootstrapform',
    'captcha',
    'registration',
    'main',
    'news',
)

# User model

AUTH_USER_MODEL = 'main.AppUser'

# Redactor settings

REDACTOR_OPTIONS = {'lang': 'ru'}
REDACTOR_UPLOAD_HANDLER = 'redactor.handlers.DateDirectoryUploader'
REDACTOR_AUTH_DECORATOR = 'django.contrib.auth.decorators.login_required'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'midnight.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'midnight/templates/demo',
            'midnight/templates/common',
        ],
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

WSGI_APPLICATION = 'midnight.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'midnight',
        'USER': 'postgres',
        'PASSWORD': 'xh48u56',
        'HOST': '192.168.56.101'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "www", "static", "bower_components"),
    os.path.join(BASE_DIR, "main", "static"),
    os.path.join(BASE_DIR, "midnight", "static", "demo"),
)

# Media storage

MEDIA_ROOT = os.path.join(BASE_DIR, 'www', 'userfiles')
MEDIA_URL = '/userfiles/'

# Assets

STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')

# Email

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/emails'

# Captcha

CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_null',)

# Registration

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
