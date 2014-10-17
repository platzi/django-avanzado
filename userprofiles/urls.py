from django.conf.urls import patterns, url

from .views import LoginView, ProfileView, PerfilRedirectView

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^perfil/$', PerfilRedirectView.as_view(), name='perfil'),
)