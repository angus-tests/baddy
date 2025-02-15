from django.urls import path
from dashboards import views
from dashboards.models import Dashboard

urlpatterns = [
    path("<slug:slug>/", views.dashboard_view, name="dashboard_view"),
]
