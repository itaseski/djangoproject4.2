from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
    # provide a proper name for the admin:
    verbose_name = "Very Academy - Ecommerce Store v1"
