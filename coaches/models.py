from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coach(models.Model):
    gender_choices = (
          ('M', 'Male'),
          ('F', 'Female'),
    )
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1000, choices=gender_choices)
    phone = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    skype = models.CharField(max_length=1000)
    description = models.TextField()


    def __unicode__(self):
         return self.user.username

# Create your models here.
