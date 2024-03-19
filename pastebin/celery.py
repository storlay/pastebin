"""
Celery config
"""

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pastebin.settings')

app = Celery('pastebin')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete_message_drive': {
        'task': 'delete_message_drive',
        'schedule': 60.0
    }
}
