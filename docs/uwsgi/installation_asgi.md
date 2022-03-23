# Levantas projecto con ASGI.
Importante:
En este metodo no funcionará el WebSocket de wsgi. Este método es para usar django channels.

Debes tener redis 5.0.7 (este solo esta disponible para ubunto 20, puede usar una instancia de vagrant o docker 
con solo la version del redis  conectar tu proyecto local al redis. Cambia la variable del settings.py __CHANNEL_LAYERS__
para apuntarlo a tu redis 5.0.7)

__1__ Activa tu entorno.
```
cd ~/Documentos/github
source env_project_websocket/bin/activate
```
__1.1__ Instala lo necesario para hacer deploy

Actualiza tu entorno o instala Daphne (ya viene en el requirements.txt)

````
pip install daphne==3.0.2
````

````
pip install -U 'Twisted[tls,http2]'
````

__2__ Instalar supervisor

    sudo apt install nginx supervisor

__2.1__ Edita tu supervisor.conf

    sudo nano /etc/supervisor/conf.d/gunicorn.conf
    
__2.2__ Pega el contenido de asgi.conf, lo encuentras en este projecto en **project_websocket/docs/supervisorctl/asgi.conf**


__2.3__ Cree el directorio de ejecución para los sockets a los que se hace referencia en el archivo de configuración del supervisor.

    sudo mkdir /run/daphne/
    
    sudo chmod -R 777 /run/daphne/
    
__2.4__ La carpeta /run/daphne/ se elimina cada vez que se reinicia el projecto, para evitar eso, creamos el archivo /usr/lib/tmpfiles.d/daphne.conf

    touch /usr/lib/tmpfiles.d/daphne.conf
    
__2.5__ Agregamos lo siguiente a /usr/lib/tmpfiles.d/daphne.conf
 
    d /run/daphne 0755

__2.6__ Hacemos que supervisorctl vuelva a leer y actualizar el archivo de configuracion

    sudo supervisorctl reread
    sudo supervisorctl update

    
__3__ Nginx

__3.1__ Crear el archivo de configuración
 
    sudo touch /etc/nginx/sites-available/project_ws_asgi
    cd /etc/nginx/sites-enabled
    sudo ln -s ../sites-available/project_ws_asgi

__3.2__ Editar el archivo __project_ws_asgi__ en sites-available

    sudo nano /etc/nginx/sites-available/project_ws_asgi
    
    
Copiar y pegar lo que hay en el archivo project_ws_asgi ubicado en __docs  > nignx > sites-available__ de este proyecto

__NOTA__ cambiar rutas de acuerdo a la ubicacion de tu proyecto.

__3.3__ Volver a cargar nginx para cargar los cambios

    sudo service nginx reload
    
__4__ Hostiamos  projectwebsocketasgi.net en local para poder ver los cambios

    sudo nano /etc/hosts

Agregar lo siguiente

    127.0.0.1    projectwebsocketasgi.net
    
__5.1__ Abrir http://projectwebsocketasgi.net/channel-example/ en tu navegador y abre la consola del navegador
veras, los mensajes imprmiendose en la consola.(Debes tener corriendo el worker celery_websocket)


