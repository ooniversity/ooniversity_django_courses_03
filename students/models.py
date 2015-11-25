# -*- coding: utf-8 -*-
from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField('Имя', max_length=50)
    slug = models.SlugField('URL', unique=True)
    surname = models.CharField('Фамилия', max_length=50)
    date_of_birth = models.DateField('Дата рождения')
    email = models.EmailField('email')
    phone = models.CharField('Телефон', max_length=30)
    address = models.CharField('Адрес', max_length=100)
    skype = models.CharField('skype', max_length=30)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.name
