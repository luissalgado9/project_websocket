from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
from .tasks import test_conexiones_websocket_tasks


def home_view(request):
    return render(request, 'home.html', {'test': "test"})


def test_conexiones_websocket_view(request):

    URL_WEBSOCKET = 'ws://projectwebsocket.net/ws/'
    origin = request.META.get('HTTP_REFERER')
    if origin == 'http://projectwebsocketmaster.net/':
        URL_WEBSOCKET = 'ws://projectwebsocketmaster.net/ws/'

    tasks = test_conexiones_websocket_tasks.delay()

    facility = tasks.id # UUID
    
    return render(request, 'test_conexiones_websocket.html', {
        'facility': facility, 
        'URL_WEBSOCKET': URL_WEBSOCKET
        })


def multiple_connections_websocket(request):
    URL_WEBSOCKET = 'ws://projectwebsocket.net/ws/'
    #URL_WEBSOCKET = "ws://127.0.0.1:8000/ws/"

    list_facility = []  # list uuid proceess
    for i in range(300):  # Get 300 UUID process, to later open multiples websocket connections
        tasks = test_conexiones_websocket_tasks.delay()
        list_facility.append(tasks.id)

    return render(request, 'multiple_connections.html', {'list_facility': list_facility, "URL_WEBSOCKET": URL_WEBSOCKET})


def raw_test_conexiones_websocket_view(request, total=None):
    """
    Genera 'n' cantidad de tareas y retorna una lista de facilities para abrir 'n' cantidad de websockets
    """
    facilities = list()
    for _ in range(total or 1):
        tasks = test_conexiones_websocket_tasks.delay()
        facilities.append(tasks.id)
    return JsonResponse({'list_facility': facilities})


def document_install_vagrant_node(request):

    if request.GET and request.GET.get('language') == 'ES':
        return render(request, 'install_vagrant_node_es.html', {})        

    return render(request, 'install_vagrant_node_eng.html', {})

def raise_error_example(request, language=None):
    title = 'Raise error example'

    if language == 'es':
        return render(request, 'raise_error_example_es.html', {'title': title,})
    
    return render(request, 'raise_error_example.html', {'title': title,})