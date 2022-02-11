### Configurar worker con supervisorctl

1.- Crear usuarios
```
sudo -i

Si ya cuenta con un usuario llamado celery omitir ese usuario
useradd -s /sbin/nologin celery

useradd -s /sbin/nologin celery_project_websocket
```

2.- Crear logs
```
    cd ~/Documentos/github/project_websocket/.logs
    mkdir celery
    cd celery
    touch project_websocket_flower.log
    touch project_websocket_error_flower.log

    sudo chmod 777 project_websocket_flower.log
    sudo chmod 777 project_websocket_error_flower.log
```

3.- Editar o crear archivo **.conf**

Crear el archivo gunicorn_ws.conf y pegar lo que hay en el archivo **gunicorn_ws_default.conf** ubicado en **docs > supervisorctl** de este proyecto

__NOTA:__ Cambiar las variables __command__, __directory__, __stdout_logfile__ y __stderr_logfile__ por las del proyecto

```
sudo nano /etc/supervisor/conf.d gunicorn_ws.conf
```

4.- Reiniciar **supervisor**:
```
    supervisorctl reread
    supervisorctl update
```

5.- Verificar el **estatus** de los workers:
```
    sudo supervisorctl status cProjectWebsocket
    sudo supervisorctl status cFlower
```