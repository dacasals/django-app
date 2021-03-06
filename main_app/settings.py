"""
Django settings for main_app project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = os.environ.get('STATIC_URL', 'static/')
STATIC_ROOT = 'static/'
# STATICFILES_DIRS = (
#   os.path.join(BASE_DIR, STATIC_URL),
# )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zpt_d(cuz4)1j6!dbo@+9!y_vuu1a852nm7&x72pk56sx$s=x1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

from dotenv import load_dotenv
project_folder = os.path.expanduser(BASE_DIR)  # adjust as appropriate

#Define environment variable to use in dependence of DEBUG flag value.
if DEBUG:
    load_dotenv(os.path.join(project_folder, 'environment.dev'))
else:
    load_dotenv(os.path.join(project_folder, 'environment.prod'))

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'corsheaders',
    'guardian',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'main_app',
    'seguridad',
    'graphqlapi'
]

GRAPHENE = {
    'SCHEMA': 'graphqlapi.schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
    'SCHEMA_OUTPUT': 'static/schema.json',  # defaults to schema.json,
    'SCHEMA_INDENT': 2,
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main_app.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'main_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME_ENV', 'main_apppy'),
        'USER': os.environ.get('DB_USER_ENV', 'root'),
        'PASSWORD': os.environ.get('DB_PASSWORD_ENV', 'explorer'),
        'HOST': os.environ.get('DB_HOST_ENV', '127.0.0.1'),
        'PORT': os.environ.get('DB_PORT_ENV', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },

}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
}

AUTHENTICATION_BACKENDS = (
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)
#
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}
# JWT_AUTH = {
#   'JWT_AUTH_COOKIE': 'jwt_auth_token',
#   'CSFR_COOKIE': True,
# }
CORS_ORIGIN_WHITELIST = [
    os.environ.get('CORS_ORIGIN_WHITELIST_ENV1', "http://wistreefw.com"),
    os.environ.get('CORS_ORIGIN_WHITELIST_ENV2', "http://localhost:8080"),
    os.environ.get('CORS_ORIGIN_WHITELIST_ENV2', "http://127.0.0.1:8080"),
    # os.environ.get('CORS_ORIGIN_WHITELIST_ENV3', "http://wistreefw.com"),
]
SPA_URL=os.environ.get('SPA_URL', "http://wistreefw.com")

DJOSER = {
    # 'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    # 'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': os.environ.get('ENV_SUB_PATH','')+'auth/users/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {},
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
