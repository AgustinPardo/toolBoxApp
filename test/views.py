from django.shortcuts import render
from django.http import HttpResponse

from .models import app

def index(request, app_name):
    actual=app.objects.get(name=app_name)
    return render(request, '../templates/front.html', {
    'title' : actual.name, 
    'description' : actual.description, 
    'texto': actual.run_app(actual.name)
    })
