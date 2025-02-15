from django.db import models
from django.contrib.auth.models import Group
from django.templatetags.static import static


class Dashboard(models.Model):
    name = models.CharField(max_length=255, unique=True)        # Name of the dashboard
    slug = models.SlugField(unique=True)                        # Slugified name of the dashboard
    short_description = models.CharField(max_length=128)        # Short description of the dashboard (for display on cards etc)
    description = models.TextField()                            # Longer description of the dashboard
    enabled = models.BooleanField(                              # Whether the dashboard is enabled or not
        default=True,
        help_text="Whether the dashboard is enabled or not")
    allowed_groups = models.ManyToManyField(                    # Groups that are allowed to view the dashboard
        Group, related_name="dashboards"
    )
    view_name = models.CharField(                               # Name of the view that renders the dashboard (stored in templates/dashboards, if not provided, the slug is used)
        max_length=255,
        null=True,
        blank=True,
        help_text="Name of the view that renders the dashboard (stored in templates/dashboards, if not provided, a view that matches the slug is expected)")

    image = models.ImageField(                                  # Image to display on the dashboard card
        upload_to="dashboards/",
        blank=True,
        null=True
    )

    def get_image_url(self):
        """Return uploaded image URL or fallback to default static image."""
        if self.image:
            return self.image.url
        return static("images/placeholder.svg")

    def __str__(self):
        return self.name
