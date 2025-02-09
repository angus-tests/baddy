"""
URL configuration for baddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from baddy import views


urlpatterns = [
    path('', views.index, name='index'),

    path('403/', views.four_three, name='403'),

    path("admin/", admin.site.urls),

    path('home/', views.home, name='home'),

    path("dashboards/", include("dashboards.urls")),  # Include dashboard-specific routes
    path("", include("accounts.urls")),  # Include account routes
]
