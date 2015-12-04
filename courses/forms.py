# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django import forms


class CourseModelForm(forms.ModelForm):
	class Meta:
		model = Course
		#exclude = ['comment', 'is_active']
		#widgets = {'package': forms.RadioSelect}
class LessonModelForm(forms.ModelForm):
	class Meta:
		model = Lesson
