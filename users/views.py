from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView

from users.forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm

User = get_user_model()


class LoginUserView(LoginView):
    """User authorization"""
    form_class = LoginUserForm
    template_name = 'login.html'


class RegisterUserView(CreateView):
    """User registration"""
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')


class UpdateUserView(UpdateView):
    """Editing a user profile"""
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordResetView(PasswordResetView):
    """Reset the user's password"""
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    """Notification about sending instructions on password reset to an email"""
    template_name = 'password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    """Entering a new password"""
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    """Notification about a successful password reset"""
    template_name = 'password_reset_complete.html'


class UserPasswordChangeView(PasswordChangeView):
    """Changing the password"""
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'password_change_form.html'


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    """Notification of successful password change"""
    template_name = 'password_change_done.html'


class DeleteProfileView(DeleteView):
    """Deleting a profile"""
    model = User
    template_name = 'delete_profile.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('users:delete_profile_done')

    def get_object(self, queryset=None):
        return self.request.user


class DeleteProfileDoneView(TemplateView):
    """Notification of successful profile deletion"""
    template_name = 'delete_profile_done.html'
