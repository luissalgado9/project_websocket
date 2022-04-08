#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_websocket.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    DIR_BASE = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(DIR_BASE, '.configs_proy/conf.json')) as json_file:
        confs = json.loads(json_file.read())

    # Vars project
    os.environ.setdefault("TIME_TASKS", confs['project']['time_task'])
    os.environ.setdefault("RAISE_ERROR_TASK", confs['project']['raise_error_tasks'])

    # Vars Urls_Websocket
    os.environ.setdefault("URL_WEBSOCKET_BALANCER", confs['urls_ws']['url_websocket_balancer'])
    os.environ.setdefault("URL_WEBSOCKET_MASTER", confs['urls_ws']['url_websocket_master'])

    # # Vars WS4REDIS
    os.environ.setdefault("WS4REDIS_CONNECTION_HOST", confs['vars_ws4redis']['ws4redis_connection_host'])
    os.environ.setdefault("HEARTBEAT_ENABLED", confs['vars_ws4redis']['heartbeat_enabled'])
    os.environ.setdefault("WS4REDIS_HEARTBEAT", confs['vars_ws4redis']['ws4redis_heartbeat'])
    os.environ.setdefault("CELERY_BROKER_URL", confs['vars_ws4redis']['celery_broker_url'])

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
