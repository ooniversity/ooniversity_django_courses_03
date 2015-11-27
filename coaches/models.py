from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    gender_choices = (('M', 'Male'), ('F', 'Female'), )
 
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    description = models.TextField()
    

    def __unicode__(self):
        return self.user.get_username()
    def get_name(self):
        return "%s" % (self.user.first_name)
    get_name.short_description = 'name'
    
    name = property(get_name)  

    def get_surname(self):
        return "%s" % (self.user.last_name)
    get_surname.short_description = 'surname'
    
    surname = property(get_surname)    
    def get_staff(self):
         return "%s" % (self.user.is_staff)
    def get_email(self):
        return "%s" % (self.user.email)
    get_email.short_description = 'email'
    email = property(get_email)
            





