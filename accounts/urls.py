from django.conf import settings
from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views


def redirect_authenticated_user(view):
    """
    If the user is authenticated, redirect to LOGIN_REDIRECT_URL.
    Otherwise, return the original view.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return view(request, *args, **kwargs)
    return wrapper


urlpatterns = [
    path('profile/', views.profile, name='profile'),  # Allow all users to access

    # Redirect logged-in users away from login and password reset pages
    path("login/", redirect_authenticated_user(auth_views.LoginView.as_view()), name="login"),
    path("password_reset/", redirect_authenticated_user(auth_views.PasswordResetView.as_view()), name="password_reset"),

    # Other auth routes remain unchanged
    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
