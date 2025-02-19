from django.urls import path

from dashboards import views

urlpatterns = [
    path("datasets/", views.dataset_dashboard, name="dataset_dashboard"),
    path("sdxhealth/", views.sdx_health_dashboard, name="sdx_health_dashboard"),
    path("secret/", views.secret_dashboard, name="secret_dashboard"),
]
