from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dataset_dashboard(request):
    return render(request, "dashboards/datasets.html")
