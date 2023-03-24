from django.urls import path

from . import views

app_name = 'dateplan'

urlpatterns = [
    path('', views.index),
]