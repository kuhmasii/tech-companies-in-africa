from django.apps import AppConfig


class IndustryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'industry'

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals
