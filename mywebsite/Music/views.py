# from django.shortcuts import render
from django.http import HttpResponse
# from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib.auth.models import User
from Music.models import Album as Album_db
from Music.models import Song as song_db
from Music import models
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
    user_li = User.objects.all()
    # di_name = {'users': }
    return render(request, "music/contactus.html", {'users': user_li})
# def AlbumDetails(requests, a_id):
#     data = Album.o


def Album(request):
    data = Album_db.objects.all()

    return render(request, "music/album.html", {'albums': data})


def AlbumDetails(request, a_id):
    try:
        data = Album_db.objects.get(id=a_id)
        return render(request, "music/albumdetails.html", {"albums": data})
    except:
        return HttpResponse("No Album Found !!!")


def SongDetails(request, al_id):
    try:
        album_obj = Album_db.objects.get(id=al_id)
        data = song_db.objects.filter(album_id=album_obj)
        return render(request, "music/songdetails.html", {"songs": data})
    except:
        return HttpResponse("No Songs Found !!!")


def CollegeAll(request):
    c_list = models.College.objects.all()
    return render(request, "college/collegeall.html", {"college": c_list})


def CollegeDetails(request, col_id):
    # c_list = models.College.objects.filter(id=col_id)
    col_obj = models.College.objects.get(id=col_id)
    stu_list = models.Students.objects.filter(college=col_obj)
    return render(request, "college/collegedetails.html", {"college": col_obj, "students": stu_list})


def StudentDetails(request, student_id):
    stu_obj = models.Students.objects.get(id=student_id)
    # print(type(stu_obj))

    col_obj = stu_obj.college

    stu_list: list = list(models.Students.objects.filter(college=col_obj))
    # print(type(stu_list[0]))
    stu_list.remove(stu_obj)
    # print(stu_list)
    # stu_list.remove()
    return render(request, "college/studentdetails.html", {"cur_student": stu_obj, "students": stu_list})
