from django.shortcuts import render, redirect
from django.conf import settings
from .models import app

from django.http import HttpResponse, Http404

import datetime

import os

def index(request, app_name):
    actual=app.objects.get(name=app_name)
    return render(request, '../templates/front.html', {
    'title' : actual.name, 
    'description' : actual.description
    })

def handle_uploaded_file(f,app_name):

    if not os.path.exists('test/'+app_name):
        os.makedirs('test/'+app_name)

    current_time = datetime.datetime.now()
    current_time = str(current_time.strftime("%X"))
    uploaded_name= str(f).split(".")[0]+"_"+current_time+"."+str(f).split(".")[1]
    path_upload="test/"+app_name+"/"
    with open(path_upload+uploaded_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return uploaded_name, current_time

def processJob(request, app_name):
    actual=app.objects.get(name=app_name)
    if request.method == 'POST':

        input_file, current_time =handle_uploaded_file(request.FILES['archivo'], app_name)
        path_upload="test/"+app_name+"/"

        actual.run_app(path_upload+input_file, path_upload+"result"+"_"+current_time)

        return redirect("job", app_name=actual.name)

    return render(request, '../templates/result.html')


def download(request, app_name):
    with open("test/salida.txt", 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text")
        response['Content-Disposition'] = 'inline; filename=download.txt'
        return response