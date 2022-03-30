from django.urls import re_path

from example_channels import consumers

websocket_urlpatterns = [
    # re_path(r'ws/channel/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/channel/(?P<uuid>[^/]+)/$', consumers.ExampleChannelsConsumer.as_asgi()),
]