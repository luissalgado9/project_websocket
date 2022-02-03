from django.shortcuts import render

# Create your views here.

def view_webscoket(request):

    return render(request, 'view_websocket.html', {})