from django.apps import AppConfig


class TracksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "muse_store.tracks"
    verbose_name = "Muse Store music tracks API"
