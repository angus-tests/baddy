from django.urls import path
from dashboards import views

urlpatterns = [
    path("<slug:slug>/", views.dashboard_view, name="dashboard_view"),
]
