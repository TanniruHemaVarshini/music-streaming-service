from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username



class Music(models.Model):
    language = models.CharField(max_length=100,blank=False)  #Telugu
    category = models.CharField(max_length=100,blank=False)  #melody
    releaseyear = models.IntegerField(blank=False) #2022
    name = models.CharField(primary_key=True,max_length=100,unique=True) #pilla raa
    movie = models.CharField(max_length=100,blank=False) #RX100
    singer = models.CharField(max_length=100,blank=False) #anurag kulkarni


    class Music:
        db_table = "music_table"

    def __str__(self):
        return self.name


class Podcasts(models.Model):
    language = models.CharField(max_length=100, blank=False)  # Telugu
    category = models.CharField(max_length=100, blank=False)  # melody
    releaseyear = models.IntegerField(blank=False)  # 2022
    name = models.CharField(primary_key=True, max_length=100,unique=True)  # pilla raa
    author = models.CharField(max_length=100, blank=False)  # anurag kulkarni

    class Podcasts:
        db_table = "podcasts_table"

    def __str__(self):
        return self.name

from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.title












