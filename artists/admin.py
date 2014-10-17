from django.contrib import admin

from .models import Artist, Album, Track

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'album')

admin.site.register(Artist)
admin.site.register(Album)