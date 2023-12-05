from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    #path('headshot', views.headshot, name = 'headshot'),
]
