from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a superuser with the provided email and password and username"

    def handle(self, *args, **kwargs):
        username = settings.ADMIN_USERNAME
        email = settings.ADMIN_EMAIL
        password = settings.ADMIN_PASSWORD

        if not username or not email or not password:
            self.stdout.write(self.style.ERROR("Please provide ADMIN_USERNAME, ADMIN_EMAIL and ADMIN_PASSWORD environment variables."))
            raise ValueError("Please provide ADMIN_USERNAME, ADMIN_EMAIL and ADMIN_PASSWORD environment variables.")

        # Create the superuser
        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists."))
