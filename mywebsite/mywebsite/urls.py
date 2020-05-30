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
from FirstApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Dy_Home),
    path('music/', Music),
    path('music/guitar', Guitar),
    path('music/Violin', Violin),
    path('music/Trumpet', Trumpet),
    path('music/Drums', Drums),
    path('music/Flute', Flute),
    path('home/', Home),
    path('name/prateek', Prateek),
    path('name/naresh', Naresh),
    path('name/nipun', Nipun),
    path('name/arnab', Arnab),
    # FirstApp
    path('name/contactus', Contactus),
    # Music
    path('music/contactus', M_Contactus),

    # Dynamic urls
    path('Dyhome/', Dy_Home),
    path('Details/<str:name>/', Details, name='Details'),
    # Songs and Albums
    # path('', MyAlbum, name='album'),
    # path("albumDetails/<int:a_id>/", AlbumDetails, name="Songs"),




]
