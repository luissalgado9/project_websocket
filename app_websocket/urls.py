from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path

from app_websocket.views import test_conexiones_websocket_view, home_view, multiple_connections_websocket

urlpatterns = [
    path('', home_view, name="home_view"),
    path('example1-ws', test_conexiones_websocket_view, name="test_conexiones_websocket_view"),
    path('example2-multiple-connections', multiple_connections_websocket, name="multiple_connections_websocket"),
]