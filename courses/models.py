# -*- coding: utf-8 -*-
from django.db import models
from coaches.models import Coach


class Course(models.Model):
    name = models.CharField('Название курса', max_length=100)
    # slug = models.SlugField('URL', unique=True)
    short_description = models.CharField('Краткле описание', max_length=250)
    description = models.TextField('Описание', blank=True)
    coach = models.ForeignKey(Coach, blank=True, null=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, blank=True, null=True, related_name='assistant_courses')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('index')


class Lesson(models.Model):
    subject = models.CharField('Тема', max_length=150)
    # slug = models.SlugField('URL', unique=True)
    description = models.TextField('Описание', blank=True)
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject
