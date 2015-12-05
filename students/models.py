from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length = 250)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 250)
    skype = models.CharField(max_length = 100)
    courses = models.ManyToManyField(Course)

    def full_name(self):
        return self.name + " " + self.surname

    def __unicode__(self):
        return self.name + " " + self.surname