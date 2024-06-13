from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "muse_store.users"
    verbose_name = "Muse Store Server API models related to users"
