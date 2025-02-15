from django.contrib import admin
from django.utils.html import format_html

from dashboards.models import Dashboard


class DashboardAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "image_preview")
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("allowed_groups",)
    readonly_fields = ("image_preview",)  # Make preview non-editable

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: contain;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Preview"


admin.site.register(Dashboard, DashboardAdmin)
