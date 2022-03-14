import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_messages_channels(uuid, text_data):
    try:
        text_data_json = json.loads(text_data)
    except TypeError:
        text_data_json = text_data
    room_group_name = '%s' % uuid
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        room_group_name,
        {
            'type': 'channel_message',
            'message': text_data_json
        }
    )
