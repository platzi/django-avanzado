from django.contrib import admin

from .models import UserTrack, UserProfile

admin.site.register(UserProfile)
admin.site.register(UserTrack)