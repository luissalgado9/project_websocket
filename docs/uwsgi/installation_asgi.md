# Levantas projecto con ASGI.
Importante:
En este metodo no funcionará el WebSocket de wsgi. Este método es para usar django channels.

Debes tener redis 5.0.7 (este solo esta disponible para ubunto 20, puede usar una instancia de vagrant o docker 
con solo la version del redis para onectar tu proyecto local al redis. Cambia la variable del settings.py __CHANNEL_LAYERS__
para apuntarlo a tu redis 5.0.7)

## SI NO TIENES REDIS 5.0.7 EN TU LOCAL (NO HACER EN PRODUCCION). SI YA LO TIENES SALTE AL PASO 2
__1.1__ Correr instancia de vagrant con ubuntu 20

    cd ~/Documentos/github
    git clone git@github.com:desarrollowh/vagrant.git
__1.2__ Edita Vagrantfile

    cd vagrant/
    sudo nano Vagrantfile

Agrega lo siguiente:

    Vagrant.configure("2") do |config|
        config.vm.box = "ubuntu/focal64"
    
        config.vm.define "ubuntu" do |ubuntu|
            ubuntu.vm.network "private_network", ip: "192.168.6.3"
            ubuntu.vm.hostname = "ubuntu"
    
        end
    
        config.ssh.insert_key = false
        config.ssh.private_key_path = ["~/Documentos/pruebas/vagrant/test_vagrant", "~/.vagrant.d/insec$
        config.vm.provision "file", source: "~/Documentos/pruebas/vagrant/test_vagrant.pub", destinatio$
    
        config.vm.synced_folder '.', '/vagrant', disabled: true
    end
__1.3__ Inicia vagrant

    vagrant up
__1.4__ Conectate a tu maquina virtual

    vagrant ssh
__1.5__ Instala redis en tu maquina virtual

    sudo apt install redis
__1.6__ Edita la configuracion de redis para aceptar conexiones remotas
    
    sudo nano /etc/redis/redis.conf
Cambia

    bind 127.0.0.1
Por
    
    bind 0.0.0.0
__1.7__ Reinicia redis

    sudo systemctl restart redis

__1.8__ En otra terminal en tu maquina virtual verifica si puedes conectarte al redis de vagrant

    redis-cli -h 192.168.6.3 PING
    
    Deberias ver la siguiente salida, si es asi, todo esta correcto
    Output:
    PONG


__2__ Activa tu entorno.
```
cd ~/Documentos/github
source env_project_websocket/bin/activate
```
__2.1__ Instala lo necesario para hacer deploy

Actualiza tu entorno o instala Daphne (ya viene en el requirements.txt)

````
pip install daphne==3.0.2
````

````
pip install -U 'Twisted[tls,http2]'
````

__3__ Instalar supervisor

    sudo apt install nginx supervisor

__3.1__ Edita tu supervisor.conf

    sudo nano /etc/supervisor/conf.d/gunicorn.conf
    
__3.2__ Pega el contenido de asgi.conf, lo encuentras en este projecto en **project_websocket/docs/supervisorctl/asgi.conf**


__3.3__ Cree el directorio de ejecución para los sockets a los que se hace referencia en el archivo de configuración del supervisor.

    sudo mkdir /run/daphne/
    
    sudo chmod -R 777 /run/daphne/
    
__3.4__ La carpeta /run/daphne/ se elimina cada vez que se reinicia el projecto, para evitar eso, creamos el archivo /usr/lib/tmpfiles.d/daphne.conf

    touch /usr/lib/tmpfiles.d/daphne.conf
    
__3.5__ Agregamos lo siguiente a /usr/lib/tmpfiles.d/daphne.conf
 
    d /run/daphne 0755

__3.6__ Hacemos que supervisorctl vuelva a leer y actualizar el archivo de configuracion

    sudo supervisorctl reread
    sudo supervisorctl update

    
__4__ Nginx

__4.1__ Crear el archivo de configuración
 
    sudo touch /etc/nginx/sites-available/project_ws_asgi
    cd /etc/nginx/sites-enabled
    sudo ln -s ../sites-available/project_ws_asgi

__4.2__ Editar el archivo __project_ws_asgi__ en sites-available

    sudo nano /etc/nginx/sites-available/project_ws_asgi
    
    
Copiar y pegar lo que hay en el archivo project_ws_asgi ubicado en __docs  > nignx > sites-available__ de este proyecto

__NOTA__ cambiar rutas de acuerdo a la ubicacion de tu proyecto.

__4.3__ Volver a cargar nginx para cargar los cambios

    sudo service nginx reload
    
__5__ Hostiamos  projectwebsocketasgi.net en local para poder ver los cambios

    sudo nano /etc/hosts

Agregar lo siguiente

    127.0.0.1    projectwebsocketasgi.net
    
__5.1__ Abrir http://projectwebsocketasgi.net/channel-example/ en tu navegador y abre la consola del navegador
veras, los mensajes imprmiendose en la consola.(Debes tener corriendo el worker celery_websocket)

