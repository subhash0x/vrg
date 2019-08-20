from django.shortcuts import render
from django.urls import path, include
from blog import views
from datetime import timedelta as tdelta

urlpatterns = [
    path('', views.post_list, name='post_list'),
]