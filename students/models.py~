from django.core.urlresolvers import reverse
from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField( max_length=225)
    surname = models.CharField(max_length=225)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=225)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
    def full_name(self):
        return self.name + " " + self.surname
    def __unicode__(self):
        return self.name + " " + self.surname
    

