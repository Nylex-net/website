"""
Django settings for nylex project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import environ
from django.urls import reverse_lazy
# from decouple import Config, Csv

# Environmental variables.
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(" ")

# LOG_DIR = os.path.join(BASE_DIR, 'logs')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',  # Log only errors and above
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django_errors.log'),
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'mozilla_django_oidc': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    },
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'App',
    'ckeditor',
    'corsheaders',
    'mozilla_django_oidc'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'mozilla_django_oidc.middleware.SessionRefresh'
]

ROOT_URLCONF = 'nylex.urls'

APPEND_SLASH = True

# For development purposes only.  For production, use the commented CORS_ALLOWED_ORIGINS instead.
# CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = ['https://ws-henry.nylex.net', 'https://www.nylex.net']

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'access-control-allow-headers',
    'access-control-allow-methods',
    'authorization',
    'content-type',
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'nylex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    #
    # The db() method is an alias for db_url().
    # 'default': env.db(),
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env('DB_HOST'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Define the directory where static files will be collected.
STATIC_ROOT = '/vol/web/static'

MEDIA_ROOT = '/vol/web/media'

# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
#     },
# }

# Expire sessions after a specific time (e.g., 30 minutes)
SESSION_COOKIE_AGE = 1800  # 30 minutes in seconds

# Expire sessions after each request (optional)
SESSION_SAVE_EVERY_REQUEST = True

# CKEDITOR_BASEPATH = join(STATIC_ROOT, "/ckeditor/ckeditor/")

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'allowedContent': True,
        'extraAllowedContent': 'data-*'
    },
}

AUTHENTICATION_BACKENDS = [
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',  # OIDC backend
    'django.contrib.auth.backends.ModelBackend',  # Fallback Django backend
]

# Configurations for Microsoft Entra ID admin login.

OIDC_RP_CLIENT_ID = env('MS_CLIENT_ID')
OIDC_RP_CLIENT_SECRET = env('MS_SECRET_VAL')
TENANT = env('MS_TENANT_ID')
OIDC_OP_AUTHORIZATION_ENDPOINT = f'https://login.microsoftonline.com/{TENANT}/oauth2/v2.0/authorize'
OIDC_OP_TOKEN_ENDPOINT = f'https://login.microsoftonline.com/{TENANT}/oauth2/v2.0/token'
OIDC_OP_USER_ENDPOINT = 'https://graph.microsoft.com/oidc/userinfo'
OIDC_OP_JWKS_ENDPOINT = f'https://login.microsoftonline.com/{TENANT}/discovery/v2.0/keys'
OIDC_RP_SIGN_ALGO = 'RS256'
# OIDC_RP_REDIRECT_URI = f'https://{env('DOMAIN')}/oidc/callback/'
# OIDC_AUTHENTICATION_CALLBACK_URL = f'https://{env('DOMAIN')}/oidc/callback/'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
OIDC_RP_SCOPES = "openid email profile"

# LOGIN_URL = '/oidc/authenticate/'
LOGIN_REDIRECT_URL = '/admin/'  # Redirect to admin after login
LOGOUT_REDIRECT_URL = '/'  # Redirect after logout
# OIDC_STORE_ACCESS_TOKEN = True
# OIDC_STORE_ID_TOKEN = True
# OIDC_STORE_REFRESH_TOKEN = True
# OIDC_CREATE_USER = False

# Redirect URIs testing with in Entra ID: /oidc/authenticate/   /oidc/callback/     /admin/