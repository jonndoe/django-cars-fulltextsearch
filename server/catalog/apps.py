from django.apps import AppConfig


class CatalogConfig(AppConfig):
    name = "catalog"

    #  Register the signal in app configuration
    def ready(self):
        from . import signals