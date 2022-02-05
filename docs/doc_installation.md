## Project test websocket

### Steps Installation



__1.1__ Crear Fork de proyecto Bitol desde __GITHUB__ y clonarlo vía ssh.

__1.2__ Clonar el proyecto anteriormente forkeado desde tu cuenta.
`cd ~/Documentos/github`
`git clone https://github.com:<username>/project_websocket.git`

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
```
pip install -r requirements.txt
pip freeze
```

__1.7__ Run Project

     cd ~/Documentos/github/project_websocket
     En una terminal con el entorno activo

     celery worker -A project_websocket --loglevel=INFO -Ofair -P gevent --concurrency=10 --queue=celery_websocket -n="celery_websocket@worker"
     
     En otra terminal con el entorno activo
     python3 manage.py runserver



__Correr proyecto con UWSGI y Nginx__

__Nginx__
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

    Copiar y pegar lo que hay en el archivo __project_ws_test__ ubicado en __docs  > nignx > sites-available__ de este proyecto

__NOTA__ cambiar rutas en __server unix__, __/static/__, __/media/__, __access_log__, __error_log__, __proxy_pass__ y __http://unix__
    
__6__ Reiniciar NGINX

    sudo nginx -t
    sudo service nginx restart
    sudo service nginx status


__Configuramos el UWSGI__

    cd ~/Documentos/github/project_websocket

__1__ Crear el archivo __bitol_uwsgi.ini__ y pegar lo que hay en el archivo __app_uwsgi.ini_default__ ubicado en __docs > uwsgi__ de este proyecto

uwsgi --ini /home/miguel-wisphub/Documentos/github/project_websocket/app_uwsgi.ini

__NOTA:__ Cambiar las variables __chdir__, __module__, __home__ y __socket__ por las del proyecto


__2__ Crear el archivo __app_websocket.ini__ y pegar lo que hay en el archivo __app_websocket.ini_default__ ubicado en __docs > uwsgi__ de este proyecto

uwsgi --ini /home/miguel-wisphub/Documentos/github/project_websocket/app_websocket.ini

__NOTA:__ Cambiar las variables __chdir__, __module__, __home__ y __socket__ por las del proyecto
