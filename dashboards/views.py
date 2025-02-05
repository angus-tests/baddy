from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render


def has_dashboard_access(user: User, required_group: str) -> bool:
    if user.is_superuser:
        return True
    return user.is_authenticated and user.groups.filter(name=required_group).exists()


@login_required
@user_passes_test(lambda u: has_dashboard_access(u, "dfts_team"))
def dataset_dashboard(request):
    return render(request, "dashboards/datasets.html")


@login_required
@user_passes_test(lambda u: has_dashboard_access(u, "sdx_team"))
def sdx_health_dashboard(request):
    return render(request, "dashboards/sdxhealth.html")


@login_required
def secret_dashboard(request):
    # Check if superuser
    if request.user.is_superuser:
        return render(request, "dashboards/secret.html")

    # Throw a 403
    return render(request, "403.html", status=403)
