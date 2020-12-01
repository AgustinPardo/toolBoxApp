from django.shortcuts import render
from django.conf import settings

from django.http import HttpResponseRedirect

from django import forms

from .models import app


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
    lineas=entrada.readlines()
    salida.write(str(len(lineas)))
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

def processJob(request,app_name):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['archivo'])
        leerlineas("test/archivo.txt")

    return render(request, '../templates/front.html')
