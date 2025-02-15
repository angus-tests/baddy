from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from dashboards.models import Dashboard
from dashboards.dependencies import get_dataset_service, get_health_service


@login_required
def dashboard_view(request, slug):
    """Dynamically loads a dashboard based on its slug."""

    # Fetch the dashboard
    dashboard = get_object_or_404(Dashboard, slug=slug)

    # Check if the user has access
    if not (request.user.is_superuser or dashboard.allowed_groups.filter(user=request.user).exists()):
        return render(request, "403.html", status=403)

    # Handle dataset dashboard
    if slug == "datasets":
        return dataset_dashboard(request, dashboard)

    # Handle SDX health dashboard
    elif slug == "sdx-health":
        return sdx_health_dashboard(request, dashboard)

    # If a view name is provided, render the view
    if dashboard.view_name:
        return render(request, f"dashboards/{dashboard.view_name}", {"dashboard": dashboard})

    # If no view name is provided, use the slug as the view name
    return render(request, f"dashboards/{slug}.html", {"dashboard": dashboard})


def dataset_dashboard(request, dashboard):
    """Handles the dataset dashboard logic."""
    number_of_results_per_page = 50

    # Load the dataset service
    dataset_service = get_dataset_service()

    # Get the search query from request
    search_query = request.GET.get("q", "").strip()

    # Fetch datasets
    datasets = dataset_service.search_datasets(search_query) if search_query else dataset_service.get_all_datasets()

    # Paginate datasets
    paginator = Paginator(datasets, number_of_results_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "dashboards/datasets.html", {"dashboard": dashboard, "dataset_page": page_obj, "search_query": search_query})


def sdx_health_dashboard(request, dashboard):
    """Handles the SDX Health dashboard logic."""
    health_service = get_health_service()
    apps = health_service.get_all_apps()
    return render(request, "dashboards/sdx_health.html", {"dashboard": dashboard, "apps": apps})
