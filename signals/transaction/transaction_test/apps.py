from django.apps import AppConfig


class TransactionTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transaction_test'

    def ready(self):
        import transaction_test.signals
