from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connection
from .models import TestModel

@receiver(post_save, sender=TestModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler running")
    sender.objects.filter(pk=instance.pk).update(processed=True)
