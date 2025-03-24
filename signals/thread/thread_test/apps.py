from django.apps import AppConfig


class ThreadTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'thread_test'

    def ready(self):
        import thread_test.signals
