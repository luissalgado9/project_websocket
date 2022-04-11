This is a test project to do debug of **django-websocket-redis**.

There are 3 possibilities to run this project

- With python manage.py & a celery worker (just like the regular django project)

![](https://i.ibb.co/Qp6Nf8F/MANAGE.png)

- With 2 wsgi applications servers & a celery worker (one application server for the **http requests** and one application server **websocket messages**) 

![](https://i.ibb.co/ZKdHfbz/serverNG.png)

- With load balancer server (pending ......)

![](https://i.ibb.co/82mhxdd/UWSGI.png)


You can run this project with manage.py and behind a wsgi app server


# RUN PROJECT WITH manage.py


### Run worker

```
cd
cd project_websocket/project_websocket/
source ../env_project_websocket/bin/activate
celery worker -A project_websocket --loglevel=INFO --queue=celery_websocket -n="ws_1@worker"
```
### Run project

```
cd
cd project_websocket/project_websocket/
source ../env_project_websocket/bin/activate
python manage.py runserver
```

# RUN PROJECT WITH WSGI


### Run worker
```
cd
cd project_websocket/project_websocket/
source ../env_project_websocket/bin/activate
celery worker -A project_websocket --loglevel=INFO --queue=celery_websocket -n="ws_1@worker"
```

### App uwsgi

```
cd
cd project_websocket/project_websocket/
source ../env_project_websocket/bin/activate
uwsgi --ini app_uwsgi.ini
```

### App websocket uwsgi

```
cd
cd project_websocket/project_websocket/
source ../env_project_websocket/bin/activate
uwsgi --ini app_websocket.ini
```

### Logs uwsgi websocket master

```
echo "" > /home/ubuntu/project_websocket/project_websocket/.logs/uwsgi/ws4redis1.log
sudo tail -f /home/ubuntu/project_websocket/project_websocket/.logs/uwsgi/ws4redis1.log
```


### Vars ENV
see documentation [here](configs.md)