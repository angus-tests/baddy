from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from dashboards.access_control import has_dashboard_access


@login_required
@user_passes_test(lambda u: has_dashboard_access(u, "dataset_dashboard"))
def dataset_dashboard(request):
    return render(request, "dashboards/datasets.html")


@login_required
@user_passes_test(lambda u: has_dashboard_access(u, "sdx_health_dashboard"))
def sdx_health_dashboard(request):
    return render(request, "dashboards/sdx_health.html")


@login_required
@user_passes_test(lambda u: has_dashboard_access(u, "secret_dashboard"))
def secret_dashboard(request):
    # Check if superuser
    if request.user.is_superuser:
        return render(request, "dashboards/secret.html")

    # Throw a 403
    return render(request, "403.html", status=403)
