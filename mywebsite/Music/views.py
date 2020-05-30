# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

# Class based view
# Def method based views
di = {'instrument': ['Guitar', 'Violin', 'Flute', 'Trumpet', 'Drums'],
      'url': ['/music/guitar', '/music/Violin', '/music/Flute', '/music/Trumpet', '/music/Drums'],
      }
details = list(zip(di['instrument'], di['url']))


def Music(request):
    return render(request, "music.html", {'details': details})

# def shhome(request):
#     return render(request,"index.html")


def Guitar(request):
    return render(request, "a/guitar.html", {'details': details})


def Violin(request):
    return render(request, "a/violin.html", {'details': details})


def Flute(request):
    return render(request, "a/flute.html", {'details': details})


def Trumpet(request):
    return render(request, "a/trumpet.html", {'details': details})


def Drums(request):
    return render(request, "a/drums.html", {'details': details})


def M_Contactus(request):
    email_q = []
    user_li = User.objects.all()
    for i in user_li:
        User.get_email_field_name()
    # di_name = {'users': }
    return render(request, "music/contactus.html", {'users': user_li})
# def AlbumDetails(requests, a_id):
#     data = Album.o
