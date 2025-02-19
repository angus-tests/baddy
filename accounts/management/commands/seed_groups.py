from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Seeds the database with default user groups and permissions"

    def handle(self, *args, **kwargs):
        groups = {
            "technical": [],
            "non-technical": [],
            "sdx": [],
            "sds": [],
            "support": [
                "view_customuser",
                "change_customuser",
                "view_group",
            ],
            "viewers": [
                "view_customuser",
                "view_group",
            ],
        }

        for group_name, permissions in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created group: {group_name}"))
            else:
                self.stdout.write(
                    self.style.WARNING(f"Group '{group_name}' already exists.")
                )

            for perm_code in permissions:
                try:
                    perm = Permission.objects.get(codename=perm_code)
                    group.permissions.add(perm)
                except Permission.DoesNotExist:
                    self.stdout.write(
                        self.style.ERROR(f"Permission '{perm_code}' not found.")
                    )

        self.stdout.write(
            self.style.SUCCESS("User groups and permissions have been seeded!")
        )
