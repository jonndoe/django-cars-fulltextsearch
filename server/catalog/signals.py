from django.contrib.postgres.search import SearchVector
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Car


# A signal will be fired every time a Car record is saved.
# Using the dispatch_uid argument on signal
# receiver function to avoid duplicate calls.
@receiver(post_save, sender=Car, dispatch_uid='on_car_save')
def on_car_save(sender, instance, *args, **kwargs):
    sender.objects.filter(pk=instance.id).update(search_vector=(
        SearchVector('variety', weight='A') +
        SearchVector('model', weight='A') +
        SearchVector('description', weight='B')
    ))