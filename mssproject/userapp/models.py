from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "user_table"

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

class Musics(models.Model):
    music_id = models.IntegerField(blank=False)
    title = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    music_director = models.CharField(max_length=100)
    language = models.CharField(max_length=100,blank=False)
    image = models.ImageField(upload_to='music/images/')
    audio_file = models.FileField(upload_to='music/audio/')


    def __str__(self):
        return str(self.music_id)+".  "+self.title
