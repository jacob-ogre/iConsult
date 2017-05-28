from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
# from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.utils import timezone

from markdownx.models import MarkdownxField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=33, default="", blank=True)
    website = models.URLField(default="", blank=True)
    bio = models.TextField(max_length=1024, default="", blank=True)
    photo = models.FileField(upload_to="uploads/", default="", blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# A basic model to hold fields for a consultation record:
class Consultation(models.Model):
    title = models.CharField(max_length=150, default="", blank=False)
    summary = MarkdownxField()
    location = models.CharField(max_length=100, default="", blank=False)
    lat = models.FloatField(default=0.0, blank=False)
    long = models.FloatField(default=0.0, blank=False)
    datum = models.CharField(max_length=100, default="NAD27", blank=False)
    area = models.FloatField(blank=False)
    area_unit = models.CharField(max_length=30, default="", blank=False)
    species = models.CharField(max_length=1000, default="", blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "consultation"

