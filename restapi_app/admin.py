from django.contrib import admin
from .models import *

# Register your models here.


class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "artist",
    ]


class TrackAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "length",
        "album",
    ]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
