from django.contrib import admin

from .models import Playlist, Track


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


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    fieldsets = [  # noqa: RUF012
        (None, {"fields": ["title", "creator"]}),
        (
            "Date information",
            {"fields": ["date_created", "date_last_modified"]},
        ),
        ("Tracks", {"fields": ["tracks"]}),
    ]
    date_hierarchy = "date_last_modified"
    list_display = ["title", "creator", "date_created"]  # noqa: RUF012
    readonly_fields = ["date_created", "date_last_modified"]  # noqa: RUF012
