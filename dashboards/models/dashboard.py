from django.db import models
from django.contrib.auth.models import Group


class Dashboard(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)  # e.g., "dataset-dashboard"
    description = models.TextField(blank=True, null=True)
    allowed_groups = models.ManyToManyField(Group, related_name="dashboards")

    def __str__(self):
        return self.name
