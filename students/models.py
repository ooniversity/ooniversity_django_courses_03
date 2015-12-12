# -*- coding:UTF-8 -*-
from django.db import models
from django.shortcuts import render
from django.core.urlresolvers import reverse
from courses.models import Course


class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=90)
    skype = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)
    
    def full_name(self):
        return self.name + " " + self.surname

    def __unicode__(self):
        return self.name + " " + self.surname

    def get_absolute_url(self):
        return reverse('students:edit', kwargs={'pk': self.pk})