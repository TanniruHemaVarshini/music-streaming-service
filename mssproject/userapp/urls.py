from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [


    path("",views.homefunction,name="userhome"),
    path("userabout",views.userabout,name="userabout"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("view",views.viewMusic,name="usermusic"),
    path("userregister",views.userregister,name="userregister"),
    path("usercontactus",views.usercontactus,name="usercontactus"),
    path("userlogout",views.userlogout,name="userlogout"),
    path("userprofile",views.userprofile,name="userprofile"),
    path("userviewmusic",views.userviewmusic,name="userviewmusic"),
    path("userviewpodcasts",views.userviewpodcasts,name="userviewpodcasts"),
    path("userplayer/",views.userplayer,name="userplayer"),
    path("usersettings",views.usersettings,name="usersettings"),
    path("firstpage",views.firstpage,name="firstpage"),
    path("firstuser",views.firstuser,name="firstuser"),
    path("firstadmin",views.firstadmin,name="firstadmin"),
    path("firstplayer",views.firstplayer,name="firstplayer"),
    path("firstabout",views.firstabout,name="firstabout"),
    path("firstuserfailed",views.firstuserfailed,name="firstuserfailed"),
    path("firstadminfailed",views.firstadminfailed,name="firstadminfailed"),
    path('<int:music_id>/',views.play_selected_music,name='play_selected_music'),
    path("musicsongs",views.musicsongs,name="musicsongs"),
    path("firstregister",views.firstregister,name="firstregister"),
    path('search/', views.search_music, name='search_music'),
    ]