from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView

from users.forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm

User = get_user_model()


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


class UserPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'password_change_form.html'


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'password_change_done.html'


class DeleteProfileView(DeleteView):
    model = User
    template_name = 'delete_profile.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('users:delete_profile_done')

    def get_object(self, queryset=None):
        return self.request.user


class DeleteProfileDoneView(TemplateView):
    template_name = 'delete_profile_done.html'
