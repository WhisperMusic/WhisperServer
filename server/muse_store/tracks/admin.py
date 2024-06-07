from django.contrib import admin

from .models import Track


class TrackAdmin(admin.ModelAdmin):
    fieldsets = [  # noqa: RUF012
        (None, {"fields": ["artist", "title"]}),
        ("Audio file", {"fields": ["audio"]}),
        ("Uploader of track", {"fields": ["uploader"]}),
    ]


admin.site.register(Track, TrackAdmin)
