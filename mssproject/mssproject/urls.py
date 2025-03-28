"""
URL configuration for mssproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("demo3",views.demofunction,name="demo"),
    path("demo",views.demofunction1,name="demo1"),
    path("demo1",views.demofunction2,name="demo2"),

    path("about",views.aboutfunction,name="about"),
    path("login",views.loginfunction,name="login"),
    path("contact",views.contactfunction,name="contact"),
    path("",include("adminapp.urls")),
    path("",include("userapp.urls")),



    #path("",include("userapp.urls")),
    #path("",include("premiumapp.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)