## Project test websocket

###Steps Installation

- Git clone
`git clone https://github.com/luissalgado9/project_websocket.git`

- Create enviroment
`virtualenv env_project_websocket -p 3.6`

- Active enviroment
`source env_project_websocket/bin/activate`

- Install dependencies
`pip install -r requirements.txt`

- In enviroment run worker
`celery worker -A project_websocket --loglevel=INFO -Ofair -P gevent --concurrency=10 --queue=celery_websocket -n="celery_websocket@worker"`

- Run server
`python manage.py runserver`