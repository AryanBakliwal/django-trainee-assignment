from django.apps import AppConfig


class SyncTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sync_test'

    def ready(self):
        import sync_test.signals