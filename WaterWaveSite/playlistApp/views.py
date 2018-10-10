from django.shortcuts import render

from .models import PlaylistSong


def index(request):
    playlist_songs = PlaylistSong.objects.all()
    context = {'playlist_songs': playlist_songs}
    return render(request, 'playlistApp/base.html', context)
