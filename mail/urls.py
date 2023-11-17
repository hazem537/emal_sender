from .views import main,contactUs,About
from django.urls import path 

urlpatterns = [
    path('',main ,name="main"),
    path('contact',contactUs ,name="contact"),
    path('about',About ,name="about"),

]