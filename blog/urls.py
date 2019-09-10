from django.shortcuts import render
from django.urls import path, include
from blog import views
from datetime import timedelta as tdelta


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('bform.html', views.bform, name='bform'),
    path('base.html', views.base, name='base'),
    # path('bform.html', views.bform, name='bform'),
    path('payment/', views.payment, name='blog-payment'),
    path('gallery.html', views.gallery, name='gallery'),
    ]
