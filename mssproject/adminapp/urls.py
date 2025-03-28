
from django.urls import path
from . import views
urlpatterns = [
    path("adminhome",views.adminhome,name="adminhome"),
    path("adminlogout",views.logout,name="adminlogout"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("viewmusic",views.viewmusic,name="viewmusic"),
    path("viewsongs",views.viewsongs,name="viewsongs"),
    path("viewpodcasts",views.viewpodcasts,name="viewpodcasts"),
    path("settings",views.settings,name="settings"),
    path("adminmusic",views.adminmusic,name="adminmusic"),
    path("adminpodcasts",views.adminpodcasts,name="adminpodcasts"),
    path("index",views.home,name="home"),
    path("addmusic",views.addmusic,name="addmusic"),
    path("addpodcasts",views.addpodcasts,name="addpodcasts"),
    path("insertmusic",views.insertmusic,name="insertmusic"),
    path("insertpodcasts",views.insertpodcasts,name="insertpodcasts"),
    path("send_otp/",views.send_otp_email, name="send_otp"),
    path("validate_otp/",views.validate_otp, name="validate_otp"),
    path('register/',views.register,name='register'),
    path('profile/',views.profile, name='profile'),
    path('login1/',views.login1, name='login1'),
    path('logout/',views.logout, name='logout'),
    path('loginfailed/',views.loginfailed, name='loginfailed'),
    path("userindex", views.userindex, name='userindex'),
    path("player/",views.player,name="player"),
    path("add",views.add,name="add"),
    path('<int:music_id>/',views.play_selected_music,name='play_selected_music'),


    path('search/', views.search_music, name='search_music'),




]