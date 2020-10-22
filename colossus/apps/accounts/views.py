from django.conf import settings as django_settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth import views as auth_views

from colossus.apps.accounts.forms import UserForm

from .models import User


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')
    extra_context = {
        'local_css_urls' : django_settings.SB_ADMIN_CLIENT_CSS_LIBRARY_URLS,
        'local_js_urls' : django_settings.SB_ADMIN_CLIENT_JS_LIBRARY_URLS
            }


    def get_object(self, queryset=None):
        return self.request.user