from django.conf.urls import patterns, url
from artists.views import AlbumListView, AlbumDetailView


urlpatterns = patterns('',
    url(r'^albums/$', AlbumListView.as_view(), name='album_list'),
    url(r'^albums/(?P<artist>[\w\-]+)/$', AlbumListView.as_view(), name='album_list'),
    url(r'^albums/detail/(?P<slug>[\w\-]+)/$', AlbumDetailView.as_view(), name='album_detail'),
)