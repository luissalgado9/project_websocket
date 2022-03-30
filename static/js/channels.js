let WEBSOCKET_URI = $("#WEBSOCKET_URI").val();
// Se crea la conexión por websocket
const chatSocket = new WebSocket(WEBSOCKET_URI);
// Cada que se recibe un mensaje se lee y se imprime en pantalla
chatSocket.onmessage = function(e) {
        receiveMessage(e.data)
        // const data = JSON.parse(e.data);
        // console.log(data)
    }
// Envia el texto "nuestro mensaje"
function sendMessage() {
    let message = "nuestro mensaje"
    chatSocket.send(JSON.stringify({
        'message': message
    }));
}
let div_error = "<div id='task_error_result' class='alert alert-danger' role='alert'>"+
                    "<h4 id='title_error_result' class='alert-heading'>Error Procesando Tarea</Tarea></h4>"+
                    "<hr>"+
                    "<p id='p_error_result'></p>"+
                    "<hr>"+
                    "<p id='extra_error_resutl' class='mb-0'></p>"+
                "</div>";
let div_jobstatic = '<div class="jobstatic-panel" class="modal" style="display: none; position: fixed; z-index: 30; padding-top: 100px; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgb(0,0,0); background-color: rgba(0,0,0,0.1);">'+
                        '<div id="caption" style="margin: auto; display: block; width: 100%; max-width: 900px; text-align: center; color: #ccc; padding: 15px 0; height: 250px;">'+
                            '<div style="background: white; margin: 0; top: 60px; padding: 15px; position: relative; text-align: center;">'+
                                '<h2 class="title-job" style="color: black; font-size: 14px;"><i class="fa fa-hourglass-start"></i><span>One moment please processing task.</span></h2>'+
                                '<h3 class="jobstatic-result" style="color: green;" >Si este mensaje no se actualiza en 2 minutos favor de reportarlo.</h3>'+
                            '</div>'+
                        '</div>'+
                    '</div>';

let div_loading_gif =   '<div id="content-loading-gif" class="loading-gif-adminolt" style="display: none; position: absolute; width: 100%; z-index: 10; top: 450px;">'+
                            '<img src="https://wisphub.net/static/img/Spin.svg" width="100" style="position: absolute; display: inline-block; left: 50%; transform: translateY(-50%);">'+
                        '</div> ';
$('body').append(div_jobstatic);
$('body').append(div_loading_gif);

let jobstatic_panel = $(".jobstatic-panel");
let jobstatic_result = $(".jobstatic-result");
let loading_gif = $("#content-loading-gif");

function receiveMessage(msg) {
    let data = JSON.parse(msg);
    data = data.message
    let status = data.status;
    if(status === "PROGRESS"){
        /*
            This keys could be send from the adminolt task
            If hideLoader key is set to True the loader will hide.
            If executeFunction key has a value (customFunction), task_function will called to manipulate data response.

            We use this keys when we have an active adminolt connection and this is sending message n times.

            example:

                for i in range(0, 30):
                    ...
                    meta = {'data': data, "status": "PROGRESS", "task_id": self.request.id}
                    publish_message_websocket(redis_publisher, meta)
                    time.sleep(5)
        */
        //
        data.hideLoader         ? loading_gif.hide()        : loading_gif.show();
        data.hideLoader         ? jobstatic_panel.hide()    : jobstatic_panel.show();
        data.executeFunction    ? task_function(data)       : null;

        //loading_gif.show();
        //jobstatic_panel.show();
        task_progress(data);


    }
    else if ( status  === "DONE") {
        if(typeof task_custom_done == 'function'){
            // Comentar sobre la fucnion task_custom_done
            // Sirve para validar si el task llamado por ajax ha terminado
            // Desde el task mandamos en el diccionario la key con la que identificaremos en la vista
            // Cual task es el que ha terminado
            // function task_custom_done(data){
            //     if(data.key_task){
            //         $('#result-get-status-code').html(data.key_task);
            //     }
            // }
            console.log('task custome done');
            task_custom_done(data)
        }else{
            console.log('task default done');
            alert(data.mensaje);
            /*task_default_done(data)*/
        }
    }
    if (status === "ERROR"){
        taks_error(data)

    }
}

function task_progress(data){
    jobstatic_result.empty().append(data.mensaje);
}