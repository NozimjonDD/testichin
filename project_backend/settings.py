"""
Django settings for mininnovation_backend project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from datetime import timedelta

from django.conf import global_settings, locale
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG') == 'TRUE'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'django_filters',
    'modeltranslation',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'mptt',
    'imagekit',
    'watson',
]

LOCAL_APPS = [
    'user',
    'common',
    'menu.apps.MenuConfig',
    'post.apps.PostConfig',
    'appeals',
    'gallery.apps.GalleryConfig',
    'contact.apps.ContactConfig',
    'survey',
    'structure.apps.StructureConfig',
    'feedback',
    'faq.apps.FaqConfig',
    'event_media_plan.apps.EventMediaPlanConfig',
    'proofreading',
]

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'watson.middleware.SearchContextMiddleware',
]

ROOT_URLCONF = 'put_here_base_project.urls'

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

WSGI_APPLICATION = 'put_here_base_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if os.getenv('IS_DOCKER') == 'TRUE':
    print(1)

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DOCKER_DB_NAME'),
            'USER': os.getenv('DOCKER_DB_USER'),
            'PASSWORD': os.getenv('DOCKER_DB_PASSWORD'),
            'HOST': os.getenv('DOCKER_DB_HOST'),
            'PORT': os.getenv('DOCKER_DB_PORT'),
        }
    }
else:
    print(2)
    if os.getenv('POSTGRES_DB') == 'TRUE':
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('POSTGRES_NAME'),
                'USER': os.getenv('POSTGRES_USER'),
                'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
                'HOST': os.getenv('POSTGRES_HOST'),
                'PORT': os.getenv('POSTGRES_PORT'),
            }
        }
    else:
        print(3)

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
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

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

gettext = lambda s: s

LANGUAGES = (
    ('uz', gettext('Uzbek')),
    ('ru', gettext('Russian')),
    ('en', gettext('English')),
    ('oz', gettext('Uzbek Cyrillic')),
    ('qr', gettext('Karakalpak')),
)

EXTRA_LANGUAGE = {
    'oz': {
        'bidi': False,
        'code': 'oz',
        'name': 'Uzbek Cyrillic',
        'name_local': 'Ўзбек',
    },
    'qr': {
        'bidi': False,
        'code': 'qr',
        'name': 'Karakalpak',
        'name_local': 'Қарақалпақ',
    }
}
locale.LANG_INFO = dict(locale.LANG_INFO, **EXTRA_LANGUAGE)

PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.User'

CORS_ORIGIN_ALLOW_ALL = True

# ---------------------------------------- Email settings-------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.put_here_base_project.uz'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 465  # for SSL
EMAIL_PORT = 587  # for TLS
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_RECEIVER_VIRTUAL_RECEPTION_AND_APPEALS_USER = os.getenv('EMAIL_RECEIVER_VIRTUAL_RECEPTION_AND_APPEALS_USER')
EMAIL_RECEIVER_VAZIR = os.getenv('EMAIL_RECEIVER_VAZIR')
EMAIL_RECEIVER_VAZIR_ORINBOSAR = os.getenv('EMAIL_RECEIVER_VAZIR_ORINBOSAR')
EMAIL_RECEIVER_PROOFREADING = os.getenv('EMAIL_RECEIVER_PROOFREADING')
EMAIL_RECEIVER_SERVICE = os.getenv('EMAIL_RECEIVER_SERVICE')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
# --------------------------------------------------------------------------------------------

# ------------------------------------ Restframework settings --------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ]
}
# --------------------------------------------------------------------------------------------

# ------------------------------------- Simple JWT settings ----------------------------------

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': os.getenv("SECRET_KEY"),
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
# --------------------------------------------------------------------------------------------