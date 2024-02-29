from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import *


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')


class UpdateUserView(UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
