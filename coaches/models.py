from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
	user = models.OneToOneField(User)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=1, 
					choices=(('M', 'Male'), ('F', 'Female'))
					)
	phone = models.CharField(max_length=12)
	email = models.EmailField(max_length=75)
	address = models.CharField(max_length=124)
	skype = models.CharField(max_length=255)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return self.user.first_name + " " + self.user.last_name

	def first_name(self):
		return self.user.first_name

	def last_name(self):
		return self.user.last_name

