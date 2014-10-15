from django.contrib.auth.models import User
from django.db import models

from artists.models import Track

class UserProfile(models.Model):
    avatar = models.ImageField(upload_to='avatars')
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

class UserTrack(models.Model):
    count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User)
    track = models.ForeignKey(Track)
