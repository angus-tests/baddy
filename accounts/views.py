from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


# Create your views here.
@require_POST
def logout_view(request):
    """Logs out the user and redirects to the index page."""
    logout(request)
    return redirect('index')


def profile(request):

    return render(request, 'accounts/profile.html')
