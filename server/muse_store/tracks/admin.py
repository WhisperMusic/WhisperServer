from django.contrib import admin

from .models import Track


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    fieldsets = [  # noqa: RUF012
        (None, {"fields": ["artist", "title"]}),
        ("Date information", {"fields": ["date_uploaded"]}),
        ("Audio file", {"fields": ["audio"]}),
        ("Uploader of track", {"fields": ["uploader"]}),
    ]
    date_hierarchy = "date_last_modified"
    list_display = ["title", "artist", "uploader", "date_uploaded"]  # noqa: RUF012
