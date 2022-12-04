"""
Django settings for localizer_project project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from drf_backend.apps import DrfBackendConfig
from pathlib import Path
import os
import os.path

Temp_Path = os.path.realpath(".")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-8q3=jdwt3d+n*n%1mb^&s%b52c8(%tf%)-tg!*!a#5gs-rs(3w"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "www.lionlocalizer.org",
    "lionlocalizer.org",
    "127.0.0.1",
    "http://lionlocalizer.org/",
    "https://lionlocalizer.org/",
    "http://lionlocalizer.org/mapping/sequence-list/"
    "http://lionlocalizer.org/mapping/align/",
]
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    # my apps
    "rest_framework",
    "drf_backend.apps.DrfBackendConfig",
    "frontend.apps.FrontendConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django_permissions_policy.PermissionsPolicyMiddleware",
    #'csp.middleware.CSPMiddleware',

   
]

PERMISSIONS_POLICY = {
    "accelerometer": [],
    "autoplay": [],
    "camera": [],
    "document-domain": [],
    "encrypted-media": [],
    "geolocation": [],
    "gyroscope": [],
    "magnetometer": [],
    "microphone": [],
    "midi": [],
    "payment": [],
    "usb": [],
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#SECURE_HSTS_SECONDS = 31536000
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_HSTS_PRELOAD = True

CSP_DEFAULT_SRC = ["'self'", 
                    'https://maps.googleapis.com/',
                    'http://lionlocalizer.org/mapping/sequence-list/',
                    'https://lionlocalizer.org/mapping/sequence-list/',
                    'http://lionlocalizer.org/mapping/align/',
                    'https://lionlocalizer.org/mapping/align/',
                    'https://lionlocalizer.org/static/frontend/main.js',
                    'https://lionlocalizer.org/static/css/index.css',

]

CSP_SCRIPT_SRC = [
    "'unsafe-eval'",
    "'unsafe-inline'",
    "'script-src-elem'",
    'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',
    'https://fonts.gstatic.com',
    'http://127.0.0.1:8000/static/frontend/main.js',
    'https://lionlocalizer.org/static/frontend/main.js',
    'http://lionlocalizer.org/static/frontend/main.js',
    'https://maps.googleapis.com/',
    'http://127.0.0.1:8000/',
    'https://127.0.0.1:8000/',
    'https://lionlocalizer.org/static/frontend/main.js',
    'https://lionlocalizer.org/static/css/index.css',
    'https://lionlocalizer.org/static/rest_framework/js/jquery-3.5.1.min.js',
    'https://lionlocalizer.org/static/rest_framework/js/ajax-form.js',
    'https://lionlocalizer.org/static/rest_framework/js/csrf.js',
    'https://lionlocalizer.org/static/rest_framework/js/bootstrap.min.js',



]

CSP_STYLE_SRC = [
    "'unsafe-inline'",
    'https://fonts.googleapis.com',
    'http://127.0.0.1:8000',
    'https://127.0.0.1:8000/',
    'http://lionlocalizer.org',
    'https://lionlocalizer.org',
    'http://127.0.0.1:8000/static/frontend/main.js',
    'https://lionlocalizer.org/static/frontend/main.js',
    'http://lionlocalizer.org/static/frontend/main.js',
    'https://lionlocalizer.org/static/css/index.css',
    'https://lionlocalizer.org/static/rest_framework/js/prettify-min.js',
    'https://lionlocalizer.org/static/rest_framework/js/default.js',
]

#CSP_SCRIPT_SRC_ELEM = [
    
#]

CSP_CONNECT_SRC = [
    'http://lionlocalizer.org/mapping/sequence-list/',
    'http://lionlocalizer.org/mapping/align/',
    'https://lionlocalizer.org/mapping/sequence-list/',
    'https://lionlocalizer.org/mapping/align/',
    'https://maps.googleapis.com',
    'https://api.emailjs.com/api/v1.0/email/send-form',
    'https://lionlocalizer.org/static/frontend/main.js',
    'https://lionlocalizer.org/static/css/index.css',
]

CSP_FONT_SRC = [
    'https://fonts.gstatic.com',
    'http://127.0.0.1:8000/static',
    'http://127.0.0.1:8000/static/rest_framework/fonts/glyphicons-halflings-regular.woff2',
    'http://127.0.0.1:8000/static/rest_framework/fonts/glyphicons-halflings-regular.woff',
    'http://127.0.0.1:8000/static/rest_framework/fonts/glyphicons-halflings-regular.ttf',
    'https://127.0.0.1:8000/static',
    'https://127.0.0.1:8000/static/rest_framework/fonts/glyphicons-halflings-regular.woff2',
    'https://127.0.0.1:8000/static/rest_framework/fonts/glyphicons-halflings-regular.woff',
    'https://127.0.0.1:8000/static/rest_framework/fonts/glyphicons-halflings-regular.ttf',
    'https://lionlocalizer.org/static/frontend/main.js',
    'https://lionlocalizer.org/static/css/index.css',
]

CSP_IMG_SRC = [
    "'self'",
    'https://fonts.googleapis.com',
    'http://127.0.0.1:8000/',
    'https://127.0.0.1:8000/',
    'https://maps.gstatic.com/',
    'https://maps.googleapis.com/',
    'data: w3.org/svg/2000',
    'https://lionlocalizer.org/static/frontend/main.js',
    'https://lionlocalizer.org/static/css/index.css',
]

CSP_OBJECT_SRC = [

]

CSP_INCLUDE_NONCE_IN = ["script-src"]

ROOT_URLCONF = "localizer_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [Temp_Path + "/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'csp.context_processors.nonce',
            ],
            
        },
    },
]

WSGI_APPLICATION = "localizer_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
