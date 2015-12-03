# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ASSETS_DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'midnight',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '192.168.56.101'
    }
}

# Email

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/emails'

# Apps

ADDITIONAL_APPS = (
    'debug_toolbar',
)
