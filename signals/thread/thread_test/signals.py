from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel
import threading

@receiver(post_save, sender=TestModel)
def signal_receiver(sender, instance, **kwargs):
    print(f"Signal Receiver Thread ID: {threading.get_ident()}")
