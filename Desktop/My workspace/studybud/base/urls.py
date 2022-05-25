from argparse import RawDescriptionHelpFormatter
from ast import Delete
from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room', views.createRoom, name='create-room'),
    path('update-room,<str:pk>/', views.updateRoom, name='update-room'),
    path('delete/<str:pk>/', views.deleteRoom, name='delete')
]