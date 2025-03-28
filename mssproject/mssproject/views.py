from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect




def demofunction(request):
    return HttpResponse("PFSD SDP PROJECT")

def demofunction1(request):
    return HttpResponse("<h3>KL University</h3>")

def demofunction2(request):
    return HttpResponse("<h3><font color='darkgrey'> MUSIC STREAMING SERVICES</font></h3>")

def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def loginfunction(request):
    return render(request,"login.html")

def contactfunction(request):
    return render(request,"contact.html")
def userabout(request):
    return render(request,"userabout.html")












