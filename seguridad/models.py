import os
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from main_app.settings import STATIC_URL


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(STATIC_URL + "avatars", filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=255, blank=True, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    zipcode = models.CharField(max_length=255, blank=True, null=False)
    country = models.CharField(max_length=255, blank=True, null=False)
    city = models.CharField(max_length=255, blank=True, null=False)
    avatar = models.ImageField(upload_to=get_file_path, null=True)
    access_code = models.IntegerField(null=True)
    account_validated = models.IntegerField(null=True)
    free_raider = models.IntegerField(blank=True, null=True)
    email_sender = models.IntegerField(blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        managed = True
        db_table = 'profile'

