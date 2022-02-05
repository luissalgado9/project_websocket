"""
WSGI config for project_websocket project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import gevent.socket
import redis.connection
redis.connection.socket = gevent.socket

os.environ.update(DJANGO_SETTINGS_MODULE='project_websocket.settings')

from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
application = uWSGIWebsocketServer()
