from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender = User)
def createUserProfile(sender, instance, created, **Kwargs):
    if created:
        Profile.objects.get_or_create(user = instance)

@receiver(post_save, sender=User)
def saveUserProfile(sender, instance, **Kwargs):
    try:
        profile, created = Profile.objects.get_or_create(user = instance)
        profile.save()
    except Exception as e:
        logger.error(f'Error saving profile for user {instance.pk}: {e}')