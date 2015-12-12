from django.db import models
from django.contrib.auth.models import User



class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    sex = [
        ('M', 'Male'),
        ('F', 'Female'),
        ]
    gender = models.CharField(max_length=2, choices=sex)
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=32)
    description = models.TextField()


    def __unicode__(self):
        return self.user.username

# Create your models here.

