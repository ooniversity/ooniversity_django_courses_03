from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, 
            choices = (('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    skype = models.CharField(max_length=50)
    description = models.TextField()

    def first_name(self, obj):
        return obj.user.first_name
    def last_name(self, obj):
        return obj.user.last_name
    
    def __unicode__(self):
        return self.user.username

   