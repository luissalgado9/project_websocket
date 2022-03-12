from channels.layers import get_channel_layer
from django.shortcuts import render
from asgiref.sync import async_to_sync


# Create your views here.


def example_django_channels(request):
    URL_WEBSOCKET = 'ws://projectwebsocket.net:8000/ws/channel/'
    print('lamo')

    uuid = 100
    name = 'fernando'
    ty = f"uuid_{uuid}"
    data = {
        'message': f'{name} Driver is now Avaliable',
        'sender': 'HQ',
        'id': str(uuid),
        'to': str(uuid),
        'type': 'DriverAvailable',
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        ty,
        {'type': 'chat_message',
         'message': data,
         }
    )

    return render(request, 'example_django_chanels.html', {'URL_WEBSOCKET': URL_WEBSOCKET})
