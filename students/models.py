# -*- coding: utf-8 -*-
import datetime
from django.db import models
from courses.models import Course
from django.core.urlresolvers import reverse

class Student(models.Model):
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length = 25, null = True, blank = True)
    address = models.CharField(max_length = 255, null = True, blank = True)
    skype = models.CharField(max_length = 255)
    courses = models.ManyToManyField(Course)
  
    def __unicode__(self):
        return ' '.join([self.name,self.surname])

    def get_absolute_url(self):
        return reverse('students:list_view')

