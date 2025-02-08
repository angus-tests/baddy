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
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "groups"),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
