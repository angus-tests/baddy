from django.urls import path

from dashboards import views

urlpatterns = [
    path("datasets/", views.dataset_dashboard, name="dataset_dashboard"),
]
