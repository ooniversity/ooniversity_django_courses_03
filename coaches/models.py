from django.db import models
from django.contrib.auth.models import User

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
