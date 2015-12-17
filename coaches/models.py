from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Coach(models.Model):
    GENDER_VALUES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_VALUES)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=50)
    description = models.TextField()
    

    def get_first_name(self):
        
        return '%s' % self.user.first_name
    first_name = property(get_first_name)

    def get_last_name(self):
        
        return '%s' % self.user.last_name
    last_name = property(get_last_name)

    def get_is_staff(self):
        
        return self.user.is_staff
    is_staff = property(get_is_staff)

    def get_email(self):
        
        return self.user.email
    email = property(get_email)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.user.username
