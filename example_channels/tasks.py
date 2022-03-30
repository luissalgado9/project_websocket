from celery import shared_task
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage
import json

from example_channels.utils import send_messages_channels


@shared_task(bind=True, queue="celery_websocket", soft_time_limit=1000)
def test_conexiones_django_channels(self):
    """
    task publish message websocket every 1 seg for 2 minutes.
    """
    import time
    count = 0

    facility = self.request.id

    print("TASK STARTED")
    start_time = time.time()
    seconds = 6  # 2 minutes
    while True:
        print("TASK PROGRESS")
        current_time = time.time()
        elapsed_time = current_time - start_time

        if count == 0:
            meta = {'mensaje': "Starting....", "status": "PROGRESS", "task_id": self.request.id}
            send_messages_channels(facility, meta)

        time.sleep(1)
        meta = {'mensaje': "'Status': 'PROGRESS' - Message # {0}".format(count), "status": "PROGRESS",
                "task_id": self.request.id}
        send_messages_channels(facility, meta)

        if elapsed_time > seconds:
            print("Finished iterating in: " + str(int(elapsed_time)) + " seconds")

            response = {
                'data': 'Hello this a example using Python-Django with Django Channels, Django Channels',
                'message': "Message finish {0}".format(count)
            }

            meta = {'response': response, "status": "DONE", "task_id": self.request.id}
            send_messages_channels(facility, meta)
            break

        count = count + 1

    print("TASK FINISHED")
    return meta
