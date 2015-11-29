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

    def _full_name(self):
        return '{0} {1}'.format(self.user.first_name, self.user.last_name)

full_name = property(_full_name)

    def email(self):
        return self.user.email