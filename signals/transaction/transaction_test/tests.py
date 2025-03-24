from django.test import TestCase
from django.db import transaction
from .models import TestModel

# Create your tests here.

class TransactionSignalTest(TestCase):
    def test_signal_runs_in_transaction(self):
        try:
            with transaction.atomic():
                TestModel.objects.create(name="test_entry")
                raise Exception("Force rollback!")
        except:
            pass
        
        exists = TestModel.objects.filter(name="test_entry").exists()
        print("Does entry exist after rollback?", exists)