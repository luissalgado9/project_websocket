## Project test websocket

### Steps Installation



__1.1__ Crear Fork de project_websocket desde __GITHUB__ y clonarlo vía ssh.

__1.2__ Clonar el proyecto anteriormente forkeado desde tu cuenta.
```
cd ~/Documentos/github
git clone git@github.com:<username>/project_websocket.git
```

__1.3__ Agregar remoto del proyecto original.

```
cd ~/Documentos/github/project_websocket
git remote add upstream git@github.com:luissalgado9/project_websocket.git
[1] Listamos los remotos del repositorio
git remote -v
```
__1.4__ Crear entorno
```
cd ~/Documentos/github
virtualenv env_project_websocket -p 3.6
```
__1.5__ Activar entorno
`source env_project_websocket/bin/activate`

__1.6__ Instalar dependiencias

    Posicionarse en el proyecto
```
 cd ~/Documentos/github/project_websocket
pip install -r requirements.txt
pip freeze
```

__1.7__ Run Project

     cd ~/Documentos/github/project_websocket
     En una terminal con el entorno activo

     celery worker -A project_websocket --loglevel=INFO --queue=celery_websocket -n="celery_websocket@worker"
     
     En otra terminal con el entorno activo
     python3 manage.py runserver


### Configurar Nginx

__Configurar Nginx para proyecto__
__1__ Actualizamos los paquetes e instalamos el nginx

     cd ~
    sudo apt-get update
    sudo apt-get install nginx

__2__ Configuramos el NGINX

__3__ Crear directorios y archivos para almacenar los logs

    sudo mkdir /etc/nginx/sites-enabled
    sudo mkdir /etc/nginx/sites-available
    
    cd ~/Documentos/github/project_websocket
    mkdir .logs
    cd .logs
    mkdir nginx
    cd nginx
    touch app.access.log
    touch app.error.log
    chmod 777 app.access.log
    chmod 777 app.error.log

__4__ Crear el archivo de configuración

    sudo touch /etc/nginx/sites-available/project_ws_test
    cd /etc/nginx/sites-enabled
    sudo ln -s ../sites-available/project_ws_test

__5__ Editar el archivo __project_ws_test__ en sites-available

    sudo nano /etc/nginx/sites-available/project_ws_test
    Copiar y pegar lo que hay en el archivo __project_ws_test__ ubicado en __docs  > nignx >        sites-available__ de este proyecto

__NOTA__ cambiar rutas en __server unix__, __/static/__, __/media/__, __access_log__, __error_log__, __proxy_pass__ y __http://unix__

__6__ Hostear dominio

    El archivo anterior project_ws_test cuenta con el dominio
    projectwebsocket.net
    Hostearlo, abrir una terminal ejecutar comando:
    sudo nano /etc/hosts
    Agregar:
    127.0.0.1   projectwebsocket.net

__6__ Reiniciar NGINX

    sudo nginx -t
    sudo service nginx restart
    sudo service nginx status


### Correr el proyecto con el UWSGI

__1__ Crear logs

    # Posicionarse en el proyecto

    cd ~/Documentos/github/project_websocket
    mkdir .logs
    cd .logs
    mkdir uwsgi
    cd uwsgi
    touch main_uwsgi.log
    touch main_websocket_uwsgi.log
    chmod 777 main_uwsgi.log
    chmod 777 main_websocket_uwsgi.log

    cd ~/Documentos/github/project_websocket

__2__ Crear el archivo __app_uwsgi.ini__ y pegar lo que hay en el archivo __app_uwsgi.ini_default__ ubicado en __docs > uwsgi__ de este proyecto

__NOTA:__ Cambiar las variables __chdir__, __module__, __home__ y __socket__ por las del proyecto

__2.1__ Run servicio uwsgi
`uwsgi --ini /home/miguel-wisphub/Documentos/github/project_websocket/app_uwsgi.ini`


__3__ Crear el archivo __app_websocket.ini__ y pegar lo que hay en el archivo __app_websocket.ini_default__ ubicado en __docs > uwsgi__ de este proyecto

__NOTA:__ Cambiar las variables __chdir__, __module__, __home__ y __socket__ por las del proyecto

__3.1__ Run servicio uwsgi
`uwsgi --ini /home/miguel-wisphub/Documentos/github/project_websocket/app_websocket.ini`



### Iniciar UWSGI como servicio systemctl

__1__. Crear archivo
`sudo nano /etc/systemd/system/app_websocket.service`

    y pegar lo que hay en el archivo __app_service_default.txt__ ubicado en __docs > systemd de este proyecto

__NOTA:__ Cambiar las variables __ExecStart__ por la ruta del archivo __app_uwsgi.ini__ de este proyecto

__2__
    Crear archivo
`sudo nano /etc/systemd/system/app_websocket_ws.service`

    y pegar lo que hay en el archivo __app_websocket_service_default.txt__ ubicado en __docs > systemd de este proyecto

__NOTA:__ Cambiar las variables __ExecStart__ por la ruta del archivo __app_websocket.ini__ de este proyecto

__3__ Iniciamos el servicio
```
sudo systemctl restart app_websocket
sudo systemctl status app_websocket

sudo systemctl restart app_websocket_ws
sudo systemctl status app_websocket_ws
```

__## Ver conexiones WS UWSGI ##__

```
sudo ps ax | grep a app_websocket
sudo lsof -p PID
````

__Que hacer si el WORKER se encola__

__1. En una terminal__

```
redis-cli
keys *
flushall
keys *
```

__2. En otra terminal__
```
ps ax | grep celery_websocket
sudo kill -9 PID
```

__3. Volver a reinciar el worker__

`celery worker -A project_websocket --loglevel=INFO --queue=celery_websocket -n="celery_websocket@worker"`