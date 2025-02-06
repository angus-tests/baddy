from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from dashboards.access_control import has_dashboard_access
from dashboards.dependencies import get_dataset_service


@login_required
@user_passes_test(lambda u: has_dashboard_access(u, "dataset_dashboard"))
def dataset_dashboard(request):

    # Load the dataset service
    dataset_service = get_dataset_service()

    # Fetch all the datasets
    datasets = dataset_service.get_all_datasets()

    # Pass the datasets to the template
    return render(request, "dashboards/datasets.html", {"datasets": datasets})


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
