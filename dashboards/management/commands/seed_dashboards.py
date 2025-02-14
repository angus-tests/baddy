from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group

from dashboards.models import Dashboard


class Command(BaseCommand):
    help = "Seeds the database with default dashboards"

    def handle(self, *args, **kwargs):
        dashboards = [
            {
                "name": "SDS Datasets",
                "slug": "datasets",
                "short_description": "View current SDS datasets",
                "description": "Here you can view all the SDC datasets and their details",
                "image_name": "dataset-dashboard.svg",
                "view_name": "datasets.html",
                "allowed_groups": ["sds"],
            },
            {
                "name": "SDX Health",
                "slug": "sdx-health",
                "short_description": "View status of SDX apps",
                "description": "Here you can view the status of all the apps in the SDX system",
                "image_name": "sdx-health-dashboard.svg",
                "view_name": "sdx_health.html",
                "allowed_groups": ["sdx"],
            },
            {
                "name": "Secret",
                "slug": "secret",
                "short_description": "A super secret dashboard",
                "description": "This is a super secret dashboard that only the super secret group can see",
                "image_name": "secret-dashboard.svg",
                "view_name": "secret.html",
                "allowed_groups": ["secret"],
            },
        ]

        for dashboard in dashboards:
            missing_groups = [
                group_name
                for group_name in dashboard["allowed_groups"]
                if not Group.objects.filter(name=group_name).exists()
            ]

            if missing_groups:
                raise CommandError(f"Missing groups: {', '.join(missing_groups)}. Please create them before running this command.")

            allowed_groups = Group.objects.filter(name__in=dashboard["allowed_groups"])

            new_dashboard, created = Dashboard.objects.get_or_create(
                name=dashboard["name"],
                slug=dashboard["slug"],
                defaults={  # Use `defaults` to prevent unnecessary updates
                    "short_description": dashboard["short_description"],
                    "description": dashboard["description"],
                    "image_name": dashboard["image_name"],
                    "view_name": dashboard["view_name"],
                },
            )
            new_dashboard.allowed_groups.set(allowed_groups)

            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Created dashboard: {dashboard['name']}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Dashboard '{dashboard['name']}' already exists."))

