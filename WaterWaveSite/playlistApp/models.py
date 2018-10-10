from django.db import models

class PlaylistSong(models.Model):
    songName = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    duration = models.FloatField()
    rating = models.IntegerField()

    def __str__(self):
        return self.songName