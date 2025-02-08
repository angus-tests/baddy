from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect if already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Get the authenticated user
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


@require_POST
def logout_view(request):
    """Logs out the user and redirects to the index page."""
    logout(request)
    return redirect('index')
