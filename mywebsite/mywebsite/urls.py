"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Music.views import *

urlpatterns = [
    path('', Home),
    path('admin/', admin.site.urls),
    path('home/', Home),
    path('home/guitar', Guitar),
    path('home/Violin', Violin),
    path('home/Trumpet', Trumpet),
    path('home/Drums', Drums),
    path('home/Flute', Flute),
    path('name/prateek', Prateek),
    path('name/naresh', Naresh),
    path('name/nipun', Nipun),
    path('name/arnab', Arnab),
    path('name/contactus', Contactus),

]
