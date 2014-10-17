from django.db import models
from django.db.models import QuerySet
from django.utils.text import slugify


class SlugMixin(object):

    def get_slug(self, text, model):
        slug_text = slugify(text)
        count = 2

        slug = slug_text
        while(model._default_manager.filter(slug=slug).exists()):
            slug = '{0}-{1}'.format(slug_text, count)

        return slug


class Artist(SlugMixin, models.Model):
    nickname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    biography = models.TextField(blank=True)
    picture = models.ImageField(upload_to='artists')
    slug = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.nickname, Artist)
        super(Artist, self).save(*args, **kwargs)


class Album(SlugMixin, models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='albums')
    slug = models.CharField(max_length=100, blank=True)
    artist = models.ForeignKey(Artist)

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.title, Album)
        super(Album, self).save(*args, **kwargs)


class TrackQuerySet(QuerySet):
    def top(self):
        return self.order_by('-listen')


class Track(SlugMixin, models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    listen = models.PositiveIntegerField(default=0)
    slug = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='tracks', blank=True, null=True)
    album = models.ForeignKey(Album)

    objects = TrackQuerySet.as_manager()

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.title, Track)
        super(Track, self).save(*args, **kwargs)
