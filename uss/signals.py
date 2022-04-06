from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from uss.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Signal for save profile
    :param sender:
    :param instance:
    :param kwargs:
    :return: new profile
    """
    instance.profile.save()
