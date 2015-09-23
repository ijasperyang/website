from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WP_IMPORTER_IMAGE_DOWNLOAD_DOMAINS = ('opencanada.centos', 'opencanada.org',
                                      'www.opencanada.org')
WP_IMPORTER_USER_PHOTO_URL_PATTERN = "http://opencanada.centos/wp-content/uploads/userphoto/{}"

WP_IMPORTER_ARTICLE_PHOTO_URL_PATTERN = "http://opencanada.centos/wp-content/uploads/{}"

IS_PRODUCTION = False

INSTALLED_APPS = INSTALLED_APPS + (
    'interactives_content',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'opencanada',
        'CONN_MAX_AGE': 600,
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
