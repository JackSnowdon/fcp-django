from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from roster.models import Wrestler

"""
Upon User creation, Profile model is added and connected to a single user
"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite_wrestler = models.ForeignKey(Wrestler, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return "{0}".format(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()