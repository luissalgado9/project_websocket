"""
WSGI config for project_websocket project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import json
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_websocket.settings')

DIR_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(DIR_BASE, '.configs_proy/conf.json')) as json_file:
    confs = json.loads(json_file.read())

    # Vars project
    os.environ.setdefault("TIME_TASKS", confs['project']['time_task'])
    os.environ.setdefault("RAISE_ERROR_TASK", confs['project']['raise_error_tasks'])

    # Vars Urls_Websocket
    os.environ.setdefault("URL_WEBSOCKET_BALANCER", confs['urls_ws']['url_websocket_balancer'])
    os.environ.setdefault("URL_WEBSOCKET_MASTER", confs['urls_ws']['url_websocket_master'])

    # Vars WS4REDIS
    os.environ.setdefault("WS4REDIS_CONNECTION_HOST", confs['vars_ws4redis']['ws4redis_connection_host'])
    os.environ.setdefault("HEARTBEAT_ENABLED", confs['vars_ws4redis']['heartbeat_enabled'])
    os.environ.setdefault("WS4REDIS_HEARTBEAT", confs['vars_ws4redis']['ws4redis_heartbeat'])
    os.environ.setdefault("CELERY_BROKER_URL", confs['vars_ws4redis']['celery_broker_url'])


application = get_wsgi_application()
