from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel
import time

@receiver(post_save, sender=TestModel)
def my_handler(sender, instance, **kwargs):
    print("Signal receiver started...")
    time.sleep(7) 
    print("Signal receiver finished after 7 seconds.")