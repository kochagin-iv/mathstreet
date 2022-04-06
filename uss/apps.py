from django.apps import AppConfig


class UssAppConfig(AppConfig):
    name = 'uss'

    def ready(self):
        import uss.signals
