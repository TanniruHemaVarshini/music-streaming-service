from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404

from .models import User, Musics
from adminapp.models import Music
from adminapp.models import Podcasts
from adminapp.models import Song
from .forms import UserRegisterForm
from adminapp.forms import SongForm


# Create your views here.


def homefunction(request):
    return render(request,"firstpage.html")
def firstuserfailed(request):
    return render(request,"firstuserfailed.html")
def firstadminfailed(request):
    return render(request,"firstadminfailed.html")
def userabout(request):
    return render(request,"userabout.html")

def userlogin(request):
    return render(request,"userlogin.html")
def userregister(request):
    return render(request,"userregister.html")
def usersettings(request):

    return render(request,"usersettings.html")
def usercontactus(request):
    return render(request,"usercontactus.html")

def userlogout(request):
    return render(request,"userlogout.html")
def musicsongs(request):
    return render(request,"musicsongs.html")
def userviewmusic(request):
    music = Musics.objects.all()
    count = Musics.objects.count()
    return render(request, "userviewmusic.html", {"music": music, "count": count})
def userviewpodcasts(request):
    podcasts = Podcasts.objects.all()
    count = Podcasts.objects.count()
    return render(request, "userviewpodcasts.html", {"podcasts": podcasts, "count": count})

def checkuserlogin(request):
    music = Musics.objects.all()
    username = request.POST["uname"]
    password = request.POST["pwd"]

    music = {
        'username': username,
        'password': password,
    }

    if music:
        return render(request,"userindex.html", music)
    else:
        return render(request,"firstuserfailed.html")

def viewMusic(request):
    music = Music.objects.all()
    count = Music.objects.count()
    return render(request, "viewmusic2.html", {"music": music, "count": count})

def userregister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created Successfully')
            return redirect('firstpage')
    else:
        form = UserRegisterForm()
    return render(request, 'userregister.html', {'form': form})
@login_required
def userprofile(request):
    return render(request, 'userprofile.html')
def firstpage(request):
    return render(request, 'firstpage.html')
def firstuser(request):
    return render(request, 'firstuser.html')
def firstregister(request):
    return render(request, 'firstregister.html')
def firstadmin(request):
    return render(request, 'firstadmin.html')
def firstplayer(request):
    return render(request, 'firstplayer.html')
def firstabout(request):
    return render(request, 'firstabout.html')

def userplayer(request):
    songs = Song.objects.all()
    form = SongForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'userplayer.html', {'songs': songs,'form': form})


def play_selected_music(request, music_id):
    music = get_object_or_404(Musics, id=music_id)

    # Find the next and previous songs
    next_song = Musics.objects.filter(id__gt=music_id).order_by('id').first()
    previous_song = Musics.objects.filter(id__lt=music_id).order_by('-id').first()

    context = {
        'music': music,
        'next_song': next_song,
        'previous_song': previous_song,
    }


    return render(request, 'musicsongs.html', context)

def search_music(request):
    query = request.GET.get('search')

    if query:
        # Perform a case-insensitive search in the 'title' field
        results = Musics.objects.filter(Q(title__icontains=query) |Q(singer__icontains=query) |Q(music_director__icontains=query)|Q(language__icontains=query))
    else:
        results = Musics.objects.all()

    context = {
        'results': results,
    }

    return render(request, 'search_music.html', context)