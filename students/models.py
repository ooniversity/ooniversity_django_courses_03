from django.db import models
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

    
