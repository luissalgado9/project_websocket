from django.shortcuts import render
from django.http import HttpResponse
from celery import shared_task
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage
import json


def test_conexiones_websocket_view(request):
    URL_WEBSOCKET = 'ws://127.0.0.1:8000/ws/' # replace your server

    facility = test_conexiones_websocket_tasks.delay()

    return render(request, 'test_conexiones_websocket.html', {'facility': facility.id, 'URL_WEBSOCKET': URL_WEBSOCKET})


@shared_task(bind=True, queue="celery_websocket", soft_time_limit=5000)
def test_conexiones_websocket_tasks(self):
    """
    publish message websocket each 5 seg for 2 minutes
    """
    import time
    count = 0

    facility = self.request.id
    redis_publisher = RedisPublisher(
        facility=facility,
        broadcast=True
    )

    meta = {'mensaje': "test message", "status": "PROGRESS", "task_id": self.request.id}
    publish_message_websocket(redis_publisher, meta)

    start_time = time.time()
    seconds = 20  # 2 minutes
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if count == 0:
            meta = {'mensaje': "Starting....", "status": "PROGRESS", "task_id": self.request.id}
            publish_message_websocket(redis_publisher, meta)

        time.sleep(1)
        count = count + 1
        meta = {'mensaje': "Message # {0}".format(count), "status": "PROGRESS", "task_id": self.request.id}
        publish_message_websocket(redis_publisher, meta)

        if elapsed_time > seconds:
            print("Finished iterating in: " + str(int(elapsed_time)) + " seconds")
            meta = {'mensaje': "Message finish {0}".format(count), "status": "DONE", "task_id": self.request.id}
            publish_message_websocket(redis_publisher, meta)
            break
    return ""


def publish_message_websocket(redis_publisher, data):
    if redis_publisher:
        redis_publisher.publish_message(RedisMessage(
            json.dumps(data)
        ))