
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    # path('room/', views.react_index, name='room'),
    path('presence-stats/', views.react_index, name='presence-stats'),
]