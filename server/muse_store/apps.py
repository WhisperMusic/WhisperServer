from django.apps import AppConfig


class MuseServerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "muse_store"
    verbose_name = "Muse Store Server's API"
