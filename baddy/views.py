from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

from django.shortcuts import render

from django.contrib.auth import logout
from django.views.decorators.http import require_POST


def index(request):

    # Redirect to the dashboards if the user is already logged in
    if request.user.is_authenticated:
        return redirect('home')

    # Otherwise, render the index page
    return render(request, 'baddy/index.html')


def four_three(request: HttpRequest) -> HttpResponse:
    """
    Render the 403 page.
    (This is a testing view, not a real view.)
    """
    return render(request, "403.html")


@login_required
def home(request):
    return render(request, 'baddy/home.html')

