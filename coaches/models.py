from django.db import models
from django.contrib.auth.models import User
import datetime

class  Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=225, choices=(("M", "Male"),("F", "Female")))
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=225)
    skype = models.CharField(max_length=50)
    description = models.TextField()
    
    def __unicode__(self):
        return self.user.username
    
    def get_full_name(self):
		return self.user.first_name + " " + self.user.last_name
