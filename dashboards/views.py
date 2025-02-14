from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from dashboards.access_control import has_dashboard_access
from dashboards.dependencies import get_dataset_service, get_health_service
from dashboards.services.sds.dataset_service import DatasetService


@login_required
@user_passes_test(lambda u: has_dashboard_access(u, "dataset_dashboard"))
def dataset_dashboard(request):

    number_of_results_per_page = 50

    # Load the sds service
    dataset_service: DatasetService = get_dataset_service()

    # Get the search query from request
    search_query = request.GET.get("q", "").strip()

    # Filter datasets if search_query exists
    if search_query:
        datasets = dataset_service.search_datasets(search_query)

    # Otherwise, get all datasets
    else:
        datasets = dataset_service.get_all_datasets()

    # Sort datasets by published_at date

    # Paginate datasets (e.g., 10 datasets per page)
    paginator = Paginator(datasets, number_of_results_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Pass the paginated object to the template
    return render(
        request,
        "dashboards/datasets.html",
        {"dataset_page": page_obj, "search_query": search_query},)


@login_required
@user_passes_test(lambda u: has_dashboard_access(u, "sdx_health_dashboard"))
def sdx_health_dashboard(request):

    # Load the health service
    health_service = get_health_service()

    # Load all the apps
    apps = health_service.get_all_apps()

    return render(request, "dashboards/sdx_health.html", {"apps": apps})


@login_required
@user_passes_test(lambda u: has_dashboard_access(u, "secret_dashboard"))
def secret_dashboard(request):
    return render(request, "dashboards/secret.html")
