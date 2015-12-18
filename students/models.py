# -*- coding: utf-8 -*-
from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255, verbose_name='СКАЙП')
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.surname

    def fullname(self):
        return self.name + ' ' + self.surname

    full_name = property(fullname)
