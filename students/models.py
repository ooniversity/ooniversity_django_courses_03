# -*- coding:UTF-8 -*-
from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length = 50)        # имя
    surname = models.CharField(max_length = 50)     # фамилия
    date_of_birth = models.DateField()              # дата рождения 
    email = models.EmailField(max_length = 254)     # e-mail
    phone = models.CharField(max_length = 20)       # телефон
    address = models.CharField(max_length = 254)    # адрес
    skype = models.CharField(max_length = 100)      # skype ID
    courses = models.ManyToManyField(Course)        # курсы, на которых учится студент

    def full_name(self):
        return self.name + " " + self.surname

    def __unicode__(self):
        return self.name + " " + self.surname
