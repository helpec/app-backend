from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import datetime


# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class HP_User(AbstractUser):
    phone = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email


class Contact(models.Model):

    user = models.ForeignKey(HP_User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return "%s - %s" % (self.user, self.name)


class Occurrence(models.Model):

    user = models.ForeignKey(HP_User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=255)

    def __str__(self):
        return "%s - %s" % (self.user, self.date_creation)
