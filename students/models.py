# -*- coding: utf-8 -*-
from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    date_of_birth = models.DateField('Дата рождения')
    email = models.EmailField('email')
    phone = models.CharField('Телефон', max_length=30)
    address = models.CharField('Адрес', max_length=100)
    skype = models.CharField('skype', max_length=30)
    courses = models.ManyToManyField(Course, verbose_name='Курсы', related_name="courses")

    def __unicode__(self):
        full_name = '%s %s' % (self.name, self.surname)
        return full_name
