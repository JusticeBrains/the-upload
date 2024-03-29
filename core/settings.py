from pathlib import Path
from django.core.management.utils import get_random_secret_key
import os
from decouple import config
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['the-upload-production.up.railway.app','127.0.0.1', 'localhost']

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
    'crispy_forms',
    'crispy_tailwind',
    'allauth',
    'allauth.account',
    'tailwind',
    'django_browser_reload',
    'compressor',

]

LOCAL_APPS = [
    'users.apps.UsersConfig',
    'upload.apps.UploadConfig',
    'pages.apps.PagesConfig',
    'theme',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'theme/templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800)
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'railway',
        'USER' :'postgres',
        'PASSWORD' : 'bAfWQTMWKba0WrkRST6Y',
        'PORT' : '7615',
        'HOST': 'containers-us-west-27.railway.app'

        # 'NAME':os.getenv('DB_NAME'),
        # 'USER' :os.getenv('DB_USER'),
        # 'PASSWORD' : os.getenv('DB_PASS'),
        # 'PORT' : os.getenv('DB_PORT'),
        # 'HOST': os.getenv('DB_HOST')
        # 'OPTIONS': {
        #     'service': 'my_service',
        #     'passfile': '.my_pgpass',
        # },
    }
}

REDIS_LOCATION = os.getenv('REDIS_LOCATION')
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDIS_LOCATION'),

    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'https://cnspfbdfpgwplfqfnexb.supabase.co/storage/v1/object/sign/the-upload/css/styles.css?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJ0aGUtdXBsb2FkL2Nzcy9zdHlsZXMuY3NzIiwiaWF0IjoxNjc0MDgwMTc2LCJleHAiOjE3MDU2MTYxNzZ9.hpaPtdp0Dv5_UHlSPCJyeAKMie-Yh440KXcyH1rExpk&t=2023-01-18T22%3A16%3A14.185Z/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'theme/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'theme/staticfiles')


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'compressor.finders.CompressorFinder',
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CustomUser
AUTH_USER_MODEL = 'users.CustomUser'

# Tailwind config
TAILWIND_APP_NAME = 'theme'

# Crispy config
CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'

INTERNAL_IPS = ['127.0.0.1', ]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = "pages:home"
ACCOUNT_LOGOUT_REDIRECT_URL = 'pages:home'
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
