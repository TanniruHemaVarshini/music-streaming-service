from django.contrib import admin
from . models import Admin,Music,Podcasts,Song
# Register your models here.
admin.site.register(Admin)
admin.site.register(Music)
admin.site.register(Podcasts)
admin.site.register(Song)
