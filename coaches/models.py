# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    skype = models.CharField('skype', max_length=30)
    description = models.TextField()

    def __unicode__(self):
        return self.user.username

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name
