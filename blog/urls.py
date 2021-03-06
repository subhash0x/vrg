from django.shortcuts import render
from django.urls import path, include
from blog import views
# import paytm.urls
from datetime import timedelta as tdelta


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('bform.html', views.bform, name='bform'),
    path('base.html', views.base, name='base'),
    # path('bform.html', views.bform, name='bform'),
    # path('payment/', views.payment, name='payment'),
    path('fee/', views.fee, name='feepayment'),
    path('gallery.html', views.gallery, name='gallery'),
	path('science.html', views.science, name='science'),
	path('homescience.html', views.homescience, name= 'homescience' ),
	path('selffinancecourses.html', views.selffinancecourses, name= 'selffinancecourses' ),
	path('arts.html', views.arts, name= 'arts' ),
	path('activites.html', views.activites, name ='activites'),
    path('contact.html', views.contact, name = 'contact'),
    path('telephonedir.html', views.telephonedir, name = 'telephonedir'),
    ]
