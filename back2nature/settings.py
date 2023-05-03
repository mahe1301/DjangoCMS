
import os

# Needed for SIMPLE_JWT
from datetime import timedelta

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2b6a+=y$+0zr6rfecy1@s7cy1gbe&!6ah8&p-1xgf#t1*v#633'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['b2nlive.b2nnetwork.com','www.b2nlive.b2nnetwork.com']


CORS_ORIGIN_ALLOW_ALL=True

# Custom user model
AUTH_USER_MODEL = "restapiservice.UserInfo"

DATE_INPUT_FORMATS = ('%d/%m/%Y','%d-%m-%Y','%Y-%m-%d')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restapiservice',
    'b2nadminapp',
    'corsheaders'
]

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),

     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12

}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    # 'http://google.com',
    # 'http://hostname.example.com',
    # 'http://localhost:8000',
    # 'http://127.0.0.1:9000',
    'https://b2nnetwork.com'#  where the requests from our React app will be #coming from.
]

ROOT_URLCONF = 'back2nature.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'back2nature.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'endingdb_livebacktonature',
        'USER': 'endingdb_b2nlivedbuser',
        'PASSWORD': 'live@b2nuser@211020',
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
)


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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = '/media/'
MEDIA_ROOT =os.path.join(BASE_DIR,'media')

# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#  ssl setting
# EMAIL_HOST = 'sng101.hawkhost.com'
# EMAIL_PORT = '465'
# EMAIL_HOST_USER = 'contact@b2nnetwork.com'
# EMAIL_HOST_PASSWORD = 'b2n@contact190820'
# EMAIL_USE_SSL = True

# non ssl setting
EMAIL_HOST = 'sng101.hawkhost.com'
# EMAIL_HOST = 'mail.b2nnetwork.com'
EMAIL_PORT = '26'
EMAIL_HOST_USER = 'contact@b2nnetwork.com'
EMAIL_HOST_PASSWORD = 'b2n@contact190820'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False


# gmail setting
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = '587'
# EMAIL_HOST_USER = '*********'
# EMAIL_HOST_PASSWORD = '*******'

# SSL the port value will have to be 465

#SSL
#https://docs.djangoproject.com/en/3.1/topics/security/


SECURE_SSL_REDIRECT = True # so that requests over HTTP are redirected to HTTPS.
SECURE_HSTS_SECONDS = 3600  #for one hour. Recommended:- 31536000 seconds, i.e. 1 year, is common
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CSRF_COOKIE_SECURE = True # This instructs the browser to only send these cookies over HTTPS connections.
CSRF_COOKIE_SAMESITE = 'Strict'

SESSION_COOKIE_SECURE = True # This instructs the browser to only send these cookies over HTTPS connections.
SECURE_BROWSER_XSS_FILTER = True  # to xss attack
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS='Deny'

CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
#SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_FRAME_DENY               = True



# B2n Logging
LOGGING={
    'version':1,
    'loggers':{
        'django':{
            'handlers':['file_handler'],
            'level':'DEBUG'
            # if propagate is set true any message to this logger will propgate to above it

        },
        'django.request': {
            'handlers': ['file_request_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server':{
            'handlers': ['file_server_handler'],
            'level': 'ERROR',
            'propagate': False,
        },

        'django.security.*': {
        'handlers': ['file_security_handler'],
        'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['file_sql_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'custom_b2n_logger': {
            'handlers': ['file_b2ncustom_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'handlers':{
        'file_handler':{
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'filename':'./logs/b2ndebug.log', 
            'formatter':'simple'
        },
        'file_request_handler':{
            'class':'logging.FileHandler',
            'filename':'./logs/b2nrequest.log', 
            'formatter':'verbose'
        },
        'file_server_handler':{
            'class':'logging.FileHandler',
            'filename':'./logs/b2nserver.log', 
            'formatter':'verbose'
        },
        'file_security_handler':{
            'class':'logging.FileHandler',
            'filename':'./logs/b2nsecurity.log', 
            'formatter':'verbose'
        },
        'file_sql_handler':{
            'class':'logging.FileHandler',
            'filename':'./logs/b2nsql.log', 
            'formatter':'verbose'
        },
        'file_b2ncustom_handler':{
            'class':'logging.FileHandler',
            'filename':'./logs/b2ncustom.log', 
            'formatter':'verbose'
        },
        'mail_admins': {
        'level': 'ERROR',
        # 'filters': ['require_debug_false'],
        'class': 'django.utils.log.AdminEmailHandler'
        }

        

    },
    'formatters':{
        'simple':{
            'format':'{levelname} {message}',
            'style': '{'
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },

    }

}