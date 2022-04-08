from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import datetime
import json

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_websocket.settings')


DIR_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(DIR_BASE, '.configs_proy/conf.json')) as json_file:
    confs = json.loads(json_file.read())

# Vars WS4REDIS
os.environ.setdefault("HEARTBEAT_ENABLED", confs['vars_ws4redis']['heartbeat_enabled'])
os.environ.setdefault("WS4REDIS_HEARTBEAT", confs['vars_ws4redis']['ws4redis_heartbeat'])
os.environ.setdefault("CELERY_BROKER_URL", confs['vars_ws4redis']['celery_broker_url'])

app = Celery('project_websocket')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


from datetime import timedelta
#Celery Monitor
app.conf.monitors_expire_success = timedelta(days=7)
app.conf.monitors_expire_error   = timedelta(days=7)
app.conf.monitors_expire_pending = timedelta(days=7)
