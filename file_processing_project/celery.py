import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_processing_project.settings')

app = Celery('file_processing_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()