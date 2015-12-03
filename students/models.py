from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    skype = models.CharField(max_length = 100)
    courses = models.ManyToManyField('courses.Course')
    def __unicode__(self):
        return self.name