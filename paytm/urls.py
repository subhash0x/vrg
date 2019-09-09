from django.urls import path,include
from paytm.views import home,payment,response
from django.conf.urls import url, include
from . import views

urlpatterns = [

   path('',views.home, name='paytm-home'),
   path('payment/',views.payment, name='paytm-payment'),
   path('response/',views.response, name='paytm-response'),
]
