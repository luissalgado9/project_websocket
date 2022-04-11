Edit: `sudo nano /home/ubuntu/project_websocket/project_websocket/.configs_proy/conf.json`

## time_task

`argument`: required_argument

`help`: Time the task is running and posting websocket messages

## raise_error_tasks

`argument`: optional

`help`: If it is "true" an error is raised when the task is publishing websocket messages, this to verify if it closes the connection or not (file_descriptor)

## celery_broker_url

`argument`: required_argument

`help` Url for celery connection with redis

## heartbeat_enabled

`argument`: optional

`help` If true, a string is assigned to the heartbeat_msg variable during the ws4redis connection in the javascript

## ws4redis_heartbeat

`argument`: optional

`help` "--heartbeat-jacob--"

## url_websocket_balancer

`argument`: required_argument

`help` If you want to do tests with the load balancer host on your pc `54.162.221.57  projectwebsocket.net`

## url_websocket_master

`argument`: required_argument

`help` If you want to do tests with the load balancer host on your pc `52.90.63.19  projectwebsocket.net`