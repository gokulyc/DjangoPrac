# from django.shortcuts import render
from django.http import HttpResponse
# from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Music.models import Album as Album_db
from Music.models import Song as song_db
from Music import models
from django.contrib.auth import login,authenticate,logout

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
    login_status=request.user.is_authenticated
    if not request.user.is_anonymous:
        login_user=request.user.username
    else:
        login_user = ''
    data = Album_db.objects.all().order_by("name")
    # data = Album_db.objects.all().order_by("-id")

    return render(request, "music/album.html", {'albums': data,'login_status':login_status,'LUSER':login_user})


def AlbumDetails(request, a_id):
    try:
        data = Album_db.objects.get(id=a_id)
        # print(type(data.img_path))
        # <class 'django.db.models.fields.files.ImageFieldFile'>
        # print(data.img_path.url)
        # /media/HalfGF.jpg

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

    return render(request, "college/studentdetails.html", {"cur_student": stu_obj, "students": stu_list})

def login_page(request,r_url):
    if request.method=='POST':
        data=request.POST
        uname=data['uname']
        pwd=data['password']
        usr=authenticate(username= uname,password=pwd)
        if usr!=None:
            login(request,usr)
            return redirect(r_url)
        else:
            print('error')


    return render(request,"auth/login.html")

def logout_site(request):
    logout(request)
    return redirect('album')


def Add_Album(request):
    if not request.user.is_authenticated:
        print(type(request.user))
        return redirect('loginpage','addAlbum')
    # print(request.method)
    if request.method == 'POST':
        print(request.POST)
        di = request.POST
        a_name = di['album_name']
        artist_name = di['artist_name']
        banner = request.FILES['artist_banner']
        obj = models.Album()
        obj.name = a_name
        obj.artist = artist_name
        obj.img_path = banner
        obj.save()
        return redirect('album')

    return render(request, "music/add_album.html")


def Add_Song(request):
    if not request.user.is_authenticated:
        print(type(request.user))
        return redirect('loginpage', 'addSong')

# 'song_name': ['fhbs'], 'album_name': ['1'], 'artist_name': ['sdvsb'], 'Year': ['2068'], 'language': ['Hindi']}
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        di = request.POST
        song_name = di['song_name']
        artist_name = di['artist_name']
        year = di['Year']
        album_id = di['album_name']
        lan = di['language']
        song_file=request.FILES['song_file']

        obj = models.Song()
        obj.name = song_name
        obj.artist = artist_name
        obj.released = year
        obj.language = lan
        obj.file=song_file

        obj.album_id = models.Album.objects.get(id=album_id)
        obj.album = models.Album.objects.get(id=album_id)
        # print(obj)
        obj.save()
        return redirect('songdetails',album_id)


    albums_d = models.Album.objects.all().order_by("name")

    return render(request, "music/add_song.html", {'albums': albums_d})
