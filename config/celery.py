import os

from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
# app.config_from_object(f'django.conf:{settings.__name__}', namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
