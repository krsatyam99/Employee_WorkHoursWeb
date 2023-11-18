from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zkteco.settings')

app = Celery('zkteco')
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'print-days-worked-every-2-minutes': {
        'task': 'attendance.tasks.print_days_worked',
        'schedule': crontab(minute='*/2'),
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")