from __future__ import absolute_import, unicode_literals

from .production import *

ROOT_URLCONF = 'opencanada.urls_admin'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

COMPRESS_URL = 'https://staging-files.opencanada.org/'
STATIC_URL = 'https://staging-files.opencanada.org/'
MEDIA_URL = 'https://staging-files.opencanada.org/'
AWS_S3_CUSTOM_DOMAIN = 'staging-files.opencanada.org'

IS_PRODUCTION = False
ADMIN_ENABLED = True

SITE_ID = 3
