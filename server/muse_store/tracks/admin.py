from django.contrib import admin

from .models import TrackModel


class TrackAdmin(admin.ModelAdmin):
    fields = ["title", "artist"]  # noqa: RUF012


admin.site.register(TrackModel, TrackAdmin)
