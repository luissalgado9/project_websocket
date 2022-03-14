from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render
from asgiref.sync import async_to_sync

from example_channels.tasks import test_conexiones_django_channels


# Create your views here.


def example_chat_django_channels(request):
    URL_WEBSOCKET = 'ws://projectwebsocket.net:8000/ws/channel/100/'

    return render(request, 'example_django_chanels.html', {'URL_WEBSOCKET': URL_WEBSOCKET})


def example_django_channels(request):
    task = test_conexiones_django_channels.delay()
    facility = task.id
    URL_WEBSOCKET = 'ws://projectwebsocket.net:8000/ws/channel/%s/' % facility

    return render(request, 'example_django_chanels.html', {'URL_WEBSOCKET': URL_WEBSOCKET})


def send_messages_channels_example(request, uuid):
    name = 'fernando'
    ty = str(uuid)
    data = {
        'message': f'{name} Driver is now Avaliable',
        'sender': 'HQ',
        'id': str(uuid),
        'to': str(uuid),
        'type': 'DriverAvailable',
    }
    channel_layer = get_channel_layer()
    # async_to_sync(channel_layer.gr)

    async_to_sync(channel_layer.group_send)(
        ty,
        {
            'type': 'channel_message',
            'message': data
        }
    )

    # print(channel_layer)
    return HttpResponse("Mensaje enviado")