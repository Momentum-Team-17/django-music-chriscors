from django.shortcuts import render
from .models import Album


def album_list(request):
    albums = Album.objects.all().order_by("title")
    return render(request, 'albums/album_list.html', {'albums': albums})
