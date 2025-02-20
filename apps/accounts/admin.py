from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "group_list", "is_staff", "is_active")
    ordering = ("username",)

    def group_list(self, obj):
        """Display all groups the user is a member of."""
        return ", ".join(group.name for group in obj.groups.all()) or "No Groups"

    group_list.short_description = "Groups"  # Column name in Django Admin

    # Ensure email appears when adding a new user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "groups",
                    "is_staff",
                ),
            },
        ),
    )

    # Get read-only fields in the change form
    def get_readonly_fields(self, request, obj=None) -> list[str]:
        # Get the current user
        user = request.user

        # If the current user is a superuser, allow editing all fields
        if user.is_superuser:
            return []

        # If the user being viewed is a superuser, prevent editing groups (unless the current user is a superuser)
        if obj.is_superuser and not user.is_superuser:
            # Return all fields as read-only
            return [
                "username",
                "password",
                "email",
                "first_name",
                "last_name",
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
                "last_login",
                "date_joined",
            ]

        # Return the default read-only fields
        return [
            "is_superuser",
            "is_staff",
            "is_active",
            "last_login",
            "date_joined",
            "user_permissions",
        ]


admin.site.register(CustomUser, CustomUserAdmin)
