from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from artists.models import Album, Track
from userprofiles.mixins import LoginRequiredMixin


class JsonResponseMixin(object):

    def response_handler(self):
        format = self.request.GET.get('format', None)
        if format == 'json':
            return self.json_to_response()

        context = self.get_context_data()
        return self.render_to_response(context)

    def json_to_response(self):
        data = self.get_data()
        return JsonResponse(data, safe=False)


class AlbumListView(LoginRequiredMixin, JsonResponseMixin, ListView):
    model = Album
    template_name = 'album_list.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return self.response_handler()

    def get_context_data(self, **kwargs):
        context = super(AlbumListView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')

        context.update({'page': page})
        return context

    def get_data(self):
        data = [{
            'cover': album.cover.url,
            'title': album.title,
            'slug': album.slug,
            'artist': album.artist.nickname,
        } for album in self.object_list]

        return data

    def get_queryset(self):
        if self.kwargs.get('artist'):
            queryset = self.model.objects.filter(artist__slug__contains=self.kwargs['artist'])
        else:
            queryset = super(AlbumListView, self).get_queryset()

        return queryset


class AlbumDetailView(LoginRequiredMixin, JsonResponseMixin, DetailView):
    model = Album
    template_name = 'album_detail.html'
    # slug_url_kwarg = 'djangoavanzado'
    # slug_field = 'title'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.response_handler()

    def get_data(self):
        data = {
            'album':{
                'cover': self.object.cover.url,
                'title': self.object.title,
                'slug': self.object.slug,
                'artist': self.object.artist.nickname,
                'tacks': [t.title for t in self.object.track_set.all()]
            }
        }

        return data


class TopTrackListView(ListView):
    queryset = Track.objects.top().filter(album__artist__slug='daft-punk')
    template_name = 'track_list.html'
