from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views
from photos.models import Album, Photo

urlpatterns = [
  url(r'^$', views.album, name='albums' ),

  url(r'^(?P<slug>[\w-]+)/$', views.photos, name='photos' ),

  #url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(
    #model=Album, context_object_name='photos',
    #template_name='photos/photo.html'), name='photos'),
]
