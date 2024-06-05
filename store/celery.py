from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# celery -A store worker --loglevel=info -P eventlet

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

app = Celery('store')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
