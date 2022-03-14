from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path

from app_websocket.views import (test_conexiones_websocket_view, home_view, multiple_connections_websocket,
    raw_test_conexiones_websocket_view, raise_error_example, document_install_vagrant_node)
from example_channels.views import example_chat_django_channels, send_messages_channels_example, example_django_channels

urlpatterns = [
    path('', home_view, name="home_view"),
    path('example1-ws', test_conexiones_websocket_view, name="test_conexiones_websocket_view"),
    path('example2-multiple-connections', multiple_connections_websocket, name="multiple_connections_websocket"),
    path('r/', raw_test_conexiones_websocket_view, name="raw_test_conexiones_websocket_view"),
    path('r/<int:total>/', raw_test_conexiones_websocket_view, name="raw_test_conexiones_websocket_view"),
    path('raise-error-example/', raise_error_example, name="raise_error_example"),
    path('raise-error-example/<str:language>/', raise_error_example, name="raise_error_example"),
    path('install-vagrant-node', document_install_vagrant_node ,name="install_vagrant_node"),
    path('chat-channel-example/', example_chat_django_channels ,name="example_chat_django_channels"),
    path('channel-example/', example_django_channels ,name="example_django_channels"),
    path('enviar-mensaje-channel/<int:uuid>/', send_messages_channels_example ,name="send_messages_channels_example"),
]