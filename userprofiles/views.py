from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView, FormView
from userprofiles.mixins import LoginRequiredMixin


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/profile/'

    def form_valid(self, form):
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = authenticate(username=username, password=password)

        login(self.request, form.user_cache)
        
        return super(LoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        is_auth = False
        name = None

        if self.request.user.is_authenticated():
            is_auth = True
            name = self.request.user.username

        data = {
            'is_auth': is_auth,
            'name': name,
        }

        context.update(data)
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            context.update({'userprofile': self.get_userprofile()})

        return context

    def get_userprofile(self):
        return self.request.user.userprofile


class PerfilRedirectView(RedirectView):
    pattern_name = 'profile'



