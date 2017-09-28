from photos.models import Album, Photo
from django.shortcuts import render_to_response

def album(request):
	albums = Album.get_all()
	return render_to_response('photos/album.html', {'albums':albums})

def photos(request, slug):
	photos = Photo.objects.filter(album__slug=slug)
	return render_to_response('photos/photo.html', {'photos':photos, 'slug':slug})
