from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path

from app_websocket.views import test_conexiones_websocket_view

urlpatterns = [
    path('', test_conexiones_websocket_view, name="test_conexiones_websocket_view"),
]