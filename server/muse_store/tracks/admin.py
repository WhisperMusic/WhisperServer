from django.contrib import admin

from .models import Track


class TrackAdmin(admin.ModelAdmin):
    fields = ["title", "artist", "audio", "uploader"]  # noqa: RUF012


admin.site.register(Track, TrackAdmin)
