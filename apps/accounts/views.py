from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


@login_required
@require_POST
def logout_view(request):
    """Logs out the user and redirects to the index page."""
    logout(request)
    return redirect("index")


@login_required
def profile(request):
    """Renders the user profile page."""
    return render(request, "accounts/profile.html")
