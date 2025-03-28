from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Admin,Music,Podcasts,Song
from django.core.mail import send_mail
import random
from django.conf import settings

from .forms import UserRegisterForm, SongForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from userapp.models import Musics

from django.core.paginator import Paginator




def userviewmusic(request):
    music = Musics.objects.all()
    count = Musics.objects.count()
    return render(request, "adminmusic.html", {"music": music, "count": count})

# Create your views here.
def adminhome(request):
    return render(request,"adminhome.html")

def home(request):
    return render(request,"index.html")
def userindex(request):
    return render(request,"userindex.html")

def checkadminlogin(request):
    adminuname = request.POST["uname"]
    adminpwd = request.POST["pwd"]

    flag = Admin.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
    print(flag)

    if flag:
        return render(request,"adminhome.html")
    else:
        return render(request,"firstadminfailed.html")

def viewmusic(request):
    music= Musics.objects.all()
    count = Musics.objects.count()
    return render(request,"viewmusic.html",{"music":music,"count":count})

def viewsongs(request):
    song=Song.objects.all()
    count = Song.objects.count()
    return render(request,"viewsongs.html",{"song":song,"count":count})

def viewpodcasts(request):
    podcasts = Podcasts.objects.all()
    count = Podcasts.objects.count()
    return render(request,"viewpodcasts.html",{"podcasts":podcasts,"count":count})

def settings(request):

    return render(request,"settings.html")

def adminmusic(request):
    music = Musics.objects.all()
    count = Musics.objects.count()
    return render(request,"adminmusic.html",{"music":music,"count":count})

def adminpodcasts(request):
    return render(request,"adminpodcasts.html")

def loginfailed(request):

    return render(request,"loginfailed.html")

def addmusic(request):
    return render(request,"addmusic.html")

def addpodcasts(request):
    return render(request,"addpodcasts.html")

def insertmusic(request):
    if request.method=="POST":
        lang = request.POST["lang"]
        category = request.POST["category"]
        ry = request.POST["ry"]
        name = request.POST['name']
        movie = request.POST["movie"]
        singer = request.POST["singer"]

        music=Music(language=lang,category=category,releaseyear=ry,name=name,movie=movie,singer=singer)
        Music.save(music)
        return HttpResponse("Music Added Successfully")


def insertpodcasts(request):
    if request.method=="POST":
        lang = request.POST["lang"]
        category = request.POST["category"]
        ry = request.POST["ry"]
        name = request.POST['name']

        author = request.POST["author"]

        podcasts=Podcasts(language=lang,category=category,releaseyear=ry,name=name,author=author)
        Podcasts.save(podcasts)
        return HttpResponse("Podcast Added Successfully")














def generate_otp():
    return str(random.randint(1000, 9999))

otp_storage = {}

def send_otp_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = generate_otp()


        otp_storage[email] = otp

        subject = 'OTP Verification'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'validate_otp.html')
    return render(request, 'send_otp.html')

def validate_otp(request):
    if request.method == 'POST':

        email = request.POST['email']
        user_otp = request.POST['otp']


        stored_otp = otp_storage.get(email)

        if user_otp == stored_otp:

            return render(request, 'adminhome.html')
        else:
            return redirect('validate_otp', msg='InValid OTP')

    return render(request, 'validate_otp.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created Successfully')
            return redirect('Users-Home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'profile.html')
def login1(request):
    return render(request, 'login1.html')
def logout(request):
    return render(request, 'logout.html')

def player(request):
    songs = Song.objects.all()
    form = SongForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'MusicPlayer.html', {'songs': songs,'form': form})


def add(request):
    return render(request,"add.html")

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


    return render(request, 'adminplayer.html', context)

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







