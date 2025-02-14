from django.db import models
from django.contrib.auth.models import Group


class Dashboard(models.Model):
    name = models.CharField(max_length=255, unique=True)        # Name of the dashboard
    slug = models.SlugField(unique=True)                        # Slugified name of the dashboard
    short_description = models.CharField(max_length=128)        # Short description of the dashboard (for display on cards etc)
    description = models.TextField()                            # Longer description of the dashboard
    allowed_groups = models.ManyToManyField(                    # Groups that are allowed to view the dashboard
        Group, related_name="dashboards"
    )
    image_name = models.CharField(max_length=255)               # Name of the image file for the dashboard (stored in the static/images/dashboards folder)
    view_name = models.CharField(max_length=255)                # Name of the view that renders the dashboard (stored in templates/dashboards)

    def __str__(self):
        return self.name
