from django.urls import path 
from . import views

urlpatterns = [
    path('meetups/',views.welcome) #our-domain.com/meetups
]
