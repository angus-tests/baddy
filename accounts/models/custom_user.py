from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    A custom user model with an additional field for user type
    """
    TECHNICAL = "technical"
    NON_TECHNICAL = "non_technical"

    USER_TYPE_CHOICES = [
        (TECHNICAL, "Technical"),
        (NON_TECHNICAL, "Non-Technical"),
    ]

    # Force users to have an email address
    email = models.EmailField(unique=True, blank=False, null=False)

    # Add a user type field
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=NON_TECHNICAL,
        help_text="Defines whether the user needs to see technical content",
    )

    def save(self, *args, **kwargs):
        """
        Ensure that an email address is set when saving a user
        """
        if not self.email:
            raise ValueError("Email address is required")
        super().save(*args, **kwargs)

    def is_technical(self):
        return self.user_type == self.TECHNICAL

    def is_non_technical(self):
        return self.user_type == self.NON_TECHNICAL
