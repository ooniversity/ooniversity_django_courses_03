from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female')
    ))
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def full_name(self):
        full_name = '{0} {1}'.format(self.user.first_name, self.user.last_name)
        return full_name

    def email(self):
        return self.user.email
