from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "user_type", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("user_type",)}),)

    # Ensure email appears when adding a new user
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "user_type", "password1", "password2"),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
