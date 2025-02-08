from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    A custom user model with an additional field for user type
    """

    # Force users to have an email address
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        help_text="Required. Used to contact a user for password resets, etc."
    )

    def save(self, *args, **kwargs):
        """
        Ensure that an email address is set when saving a user
        """
        if not self.email:
            raise ValueError("Email address is required")
        super().save(*args, **kwargs)

    def is_technical(self) -> bool:
        """
        Check to see if this user is in the technical group
        :return:
        """
        return self.groups.filter(name="technical").exists()

    def is_non_technical(self) -> bool:
        """
        Check to see if this user is in the non-technical group
        :return:
        """
        return self.groups.filter(name="non-technical").exists()
