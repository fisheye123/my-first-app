from django.contrib import admin
from photos.models import Album, Photo

class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'slug', 'img']})
    ]
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}
    ordering = ['title']

class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['title', 'album', 'img']})
    ]
    list_display = ['title', 'album']
    ordering = ['title']

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
