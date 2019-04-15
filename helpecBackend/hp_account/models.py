from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime


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
        
