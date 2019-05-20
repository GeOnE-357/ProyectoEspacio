"""
Django settings for espacio project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!v0$k0sa6^p^!*_yir=!3_$=f@b9kd8p)r#h$*=2l!*reo=_fv'

# SECURITY WARNING: don't run with debug turned on in production!

#DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dependencia',
    'personas',
    'cursos',
    'control',
    'django_filters',
    'asistencia',
    'importacion',
    #'mod_wsgi.server',
]

LOGGING = {
    'version':1,
    'disable_existing_logger':False,
    'handlers': {
        'console':{
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django':{
            'handlers':['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO')
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'espacio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #Agregada la direccion de "templates".
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

WSGI_APPLICATION = 'espacio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        
        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'gestionedlt_db',
        #'USER': 'gestionedlt_db',
        #'PASSWORD': 'lzmSTSkQCu',
        #'HOST': 'localhost',
        #'PORT': '3306',
        
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'espacio',
        'USER': 'root',
        'PASSWORD': 'keeponrock357',
        'HOST': 'localhost',
        'PORT': '3306',
    }
    }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
#AUTH_USER_MODEL = 'core.User'

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

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Ushuaia'

DATE_FORMAT = "d-m-Y"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, "static")]
#STATIC_ROOT =os.path.join(BASE_DIR, "static")