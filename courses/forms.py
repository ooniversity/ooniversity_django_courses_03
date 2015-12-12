# -*- coding: utf-8 -*-
from django.forms import ModelForm
from courses.models import Course
from courses.models import Lesson
from django import forms

class CourseModelForm(ModelForm):
    
    class Meta:
        model = Course
        fields = '__all__'

class LessonModelForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
