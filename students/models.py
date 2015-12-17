from django.db import models
<<<<<<< HEAD
from courses.models import Course



class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, default='12-34-56')
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
    
    def get_full_name(self):
        return '%s %s' % (self.name, self.surname)
    full_name = property(get_full_name)

    
=======

from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.name



>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
