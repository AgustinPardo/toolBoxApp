from django.urls import path

from . import views

urlpatterns = [
    path('<str:app_name>/', views.index, name='index'),
    path('<str:app_name>/job', views.processJob, name='job'),
    path('<str:app_name>/download', views.download, name='download'),
]
