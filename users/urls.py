"""
Users URLs configuration
"""

from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (
    DeleteProfileDoneView,
    DeleteProfileView,
    LoginUserView,
    RegisterUserView,
    UpdateUserView,
    UserPasswordChangeDoneView,
    UserPasswordChangeView,
    UserPasswordResetCompleteView,
    UserPasswordResetConfirmView,
    UserPasswordResetDoneView,
    UserPasswordResetView,
)

urlpatterns = [
    path(
        "login/",
        LoginUserView.as_view(),
        name="login"
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout"
    ),
    path(
        "register/",
        RegisterUserView.as_view(),
        name="register"
    ),
    path(
        "profile/",
        UpdateUserView.as_view(),
        name="profile"
    ),

    path(
        "password-change/",
        UserPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password-change/done/",
        UserPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "password-reset/",
        UserPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        UserPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        UserPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),

    path(
        "delete-profile/", DeleteProfileView.as_view(), name="delete_profile"
    ),
    path(
        "delete-profile/done/",
        DeleteProfileDoneView.as_view(),
        name="delete_profile_done",
    ),
]
