import os

import django
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
import example_channels.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mychannels.settings")
django.setup()

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            example_channels.routing.websocket_urlpatterns
        )
    ),
})