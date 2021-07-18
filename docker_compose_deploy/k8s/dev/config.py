from settings.common import *

# for multi computer room deploy and use separate redis server
DEPLOY_ZONE = ''

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm$*&&u*9+-$g^b9lj0)**1$0$wfh1wk$ye^4p+s)cera)g3fml'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

MIDDLEWARE = [
    'service.csrf_service.DisableCSRF',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'service.permission.api_permission.ApiPermissionCheck',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'loonflow',  # Or path to database file if using sqlite3.
            'USER': 'root',  # Not used with sqlite3.
            'PASSWORD': 'root',  # Not used with sqlite3.
            'HOST': '192.168.1.160',  # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '46039',  # Set to empty string for default. Not used with sqlite3.
        }
}

REDIS_HOST = 'redis.ops'
REDIS_PORT = 6379
REDIS_DB = 10
REDIS_PASSWORD = 'hose_ops'

if REDIS_PASSWORD:
    CELERY_BROKER_URL = 'redis://:{}@{}:{}/{}'.format(REDIS_PASSWORD, REDIS_HOST, REDIS_PORT, REDIS_DB)
else:
    CELERY_BROKER_URL = 'redis://{}:{}/{}'.format(REDIS_HOST, REDIS_PORT, REDIS_DB)

LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'formatters': {
            'standard': {
                'format': '%(asctime)s %(pathname)s process-%(process)d thread-%(thread)d %(lineno)d [%(levelname)s]: %(message)s',
            },
        },
        'handlers': {
            'file_handler': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': HOMEPATH + '/loonflow.log',
                'formatter': 'standard'
            },
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file_handler', "console"],
                'propagate': True,
                'level': 'DEBUG',
                        },
            'django.db.backends': {
                'handlers': ['console'],
                'propagate': True,
                'level': 'INFO',
            }
        }
    }