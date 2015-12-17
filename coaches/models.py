from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD

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
=======
<<<<<<< HEAD
class Coach(models.Model): 
    user = models.OneToOneField(User) 
    date_of_birth = models.DateField() 
    GENDER = ( 
        ('M', 'Male'), 
        ('F', 'Female'), 
    ) 
    gender = models.CharField(choices=GENDER, max_length=6) 
    phone = models.CharField(max_length=15) 
    address = models.CharField(max_length=255) 
    skype = models.CharField(max_length=255) 
    description = models.TextField() 

    def __unicode__(self): 
        return self.user.username
=======

>>>>>>> fb8e773dc2544433f2f086ca476591072179281d
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
