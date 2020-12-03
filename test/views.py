from django.shortcuts import render, redirect
from django.conf import settings
from .models import app

from django.http import HttpResponse, Http404

def index(request, app_name):
    actual=app.objects.get(name=app_name)
    return render(request, '../templates/front.html', {
    'title' : actual.name, 
    'description' : actual.description, 
    'texto': actual.run_app(actual.name)
    })

def handle_uploaded_file(f):
    with open('test/archivo.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def leerlineas(file):
    entrada=open(file,"r")
    salida=open("test/salida.txt", "w")
    salida.write(str(len(entrada.readlines())))
    entrada.close()
    salida.close()
    return 0

def cabecera(file):
    entrada=open(file,"r")
    salida=open("test/salida.txt","w")
    salida.write(entrada.readlines()[0])
    entrada.close()
    salida.close()
    return 0

def timeTest():
    import time
    start = time. time()
    time.sleep(7)
    salida=open("test/salida.txt","w")
    end = time. time()
    salida.write(str(end-start))
    salida.close()
    return 0

def processJob(request, app_name):
    actual=app.objects.get(name=app_name)
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['archivo'])
        timeTest()
        leerlineas("test/archivo.txt")
        return redirect("job", app_name=actual.name)

    return render(request, '../templates/result.html')


def download(request, app_name):
    with open("test/salida.txt", 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text")
        response['Content-Disposition'] = 'inline; filename=download.txt'
        return response