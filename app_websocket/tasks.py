from celery import shared_task
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage
import json

@shared_task(bind=True, queue="celery_websocket", soft_time_limit=1000)
def test_conexiones_websocket_tasks(self):
    """
    task publish message websocket every 1 seg for 2 minutes.
    """
    import time
    count = 0

    facility = self.request.id
    redis_publisher = RedisPublisher(
        facility=facility,
        broadcast=True
    )

    print("TASK STARTED")
    start_time = time.time()
    seconds = 20  # 2 minutes
    while True:
        print("TASK PROGRESS")
        current_time = time.time()
        elapsed_time = current_time - start_time

        if count == 0:
            meta = {'mensaje': "Starting....", "status": "PROGRESS", "task_id": self.request.id}
            publish_message_websocket(redis_publisher, meta)

        time.sleep(1)
        meta = {'mensaje': "'Status': 'PROGRESS' - Message # {0}".format(count), "status": "PROGRESS", "task_id": self.request.id}
        publish_message_websocket(redis_publisher, meta)

        if elapsed_time > seconds:
            print("Finished iterating in: " + str(int(elapsed_time)) + " seconds")
            
            response = {
            'data': 'Hello this a example using Python-Django with Websocket, WS4Redis',
            'message': "Message finish {0}".format(count)
            }

            meta = {'response': response, "status": "DONE", "task_id": self.request.id}
            publish_message_websocket(redis_publisher, meta)
            break

        count = count + 1

    print("TASK FINISHED")
    return meta


def publish_message_websocket(redis_publisher, data):
    if redis_publisher:
        redis_publisher.publish_message(RedisMessage(
            json.dumps(data)
        ))