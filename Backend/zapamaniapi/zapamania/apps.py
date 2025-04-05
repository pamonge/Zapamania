from django.apps import AppConfig


class ZapamaniaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zapamania'

    def ready(self):
        import zapamania.signals