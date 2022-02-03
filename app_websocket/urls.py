from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path

from app_websocket.views import view_webscoket

urlpatterns = [
    path('', view_webscoket, name="view_webscoket"),
]