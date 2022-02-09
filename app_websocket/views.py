from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_conexiones_websocket_tasks

def home_view(request):
    return render(request, 'home.html', {'test': "test"})

def test_conexiones_websocket_view(request):
    URL_WEBSOCKET = 'ws://projectwebsocket.net/ws/'
    #URL_WEBSOCKET = "ws://127.0.0.1:8000/ws/"
    # Publish message websocket every 1 seg for 2 minutes.
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

    return render(request, 'multiple_connections.html', {'list_facility': list_facility})