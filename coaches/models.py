from django.db import models

from django.contrib.auth.models import User

class Coach (models.Model):
    user = models.OneToOneField (User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices = (('M','Male'), ('F','Female')))
    description = models.TextField()
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    
    def  __unicode__(self):
	return self.user.username
    
    def surname(self):
        return self.user.last_name
    
    def name(self):
        return self.user.first_name

    def full_name(self):
        full_name = '%s %s' % (self.user.first_name, self.user.last_name)
        return full_name

    def email(self):
        return self.user.email