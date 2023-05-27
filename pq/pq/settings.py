


TIME_ZONE = 'Asia/Ho_Chi_Minh'"""
Django settings for pq project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-erv=!0qz$e6f5zgrvq)m4j31=an)uip-p9&t7j5ms#ygwqx9hw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['pq.vnsp.vn']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'set',
    'pq',
    'cs',
    'sa',
    'django_filters',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pq.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'pq.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "PQ",
        "USER": "sa",
        "PASSWORD": "Vsp$2015",
        "HOST": "192.168.0.6",
        "PORT": "1433",
        # 'CONN_MAX_AGE': 600,  # Maximum age of connections: 10 minutes
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",
            'extra_params': 'MARS_Connection=Yes', 
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

IMPORT_EXPORT_USE_TRANSACTIONS = True
# TIME_ZONE = 'Asia/Ho_Chi_Minh'

LOGOUT_REDIRECT_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")     
# Command need to take for picture display is: 
# sudo chmod 777 -R /home/hungnt/pq.vnsp.vn/pq/media
# sudo chown -R www-data:www-data /home/hungnt/pq.vnsp.vn/pq/media


# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = BASE_DIR / "sent_emails"    sudo chmod 777 -R /home/hungnt/pq.vnsp.vn/pq/sent_emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail25542.maychuemail.com'  
EMAIL_USE_TLS = None
EMAIL_PORT = 25
EMAIL_HOST_USER = 'support@vnsp.vn'
EMAIL_HOST_PASSWORD = 'fdc5ccHa1'
DEFAULT_FROM_EMAIL = 'support@vnsp.vn'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'