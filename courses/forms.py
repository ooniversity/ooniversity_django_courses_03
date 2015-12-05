# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from courses.models import Course, Lesson
from coaches.models import Coach


class CourseModelForm(forms.ModelForm):
    class Meta:
    	model = Course
    	
class LessonModelForm(forms.ModelForm):
    class Meta:
    	model = Course
