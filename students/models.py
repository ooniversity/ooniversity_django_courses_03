from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    skype = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)
