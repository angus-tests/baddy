from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

from django.shortcuts import render

from django.contrib.auth import logout
from django.views.decorators.http import require_POST


@require_POST
def logout_view(request):
    """Logs out the user and redirects to the index page."""
    logout(request)
    return redirect('index')


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect if already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Get the authenticated user
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('dashboard')  # Redirect after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'baddy/index.html', {'form': form})


def dashboard(request):
    # TODO add authentication check
    return render(request, 'baddy/dashboard.html')


def four_three(request: HttpRequest) -> HttpResponse:
    """
    Render the 403 page.
    (This is a testing view, not a real view.)
    """
    return render(request, "403.html")
