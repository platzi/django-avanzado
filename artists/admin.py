from django.contrib import admin

from .models import Artist, Album, Track

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)