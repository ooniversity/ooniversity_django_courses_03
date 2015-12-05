# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from students.models import Student, CourseApplication
from courses.models import Course, Lesson
from django import forms
from django.contrib import messages


class StudentModelForm(forms.ModelForm):
	class Meta:
		model = Student
        fields = '__all__'
		#exclude = ['comment', 'is_active']
		#widgets = {'package': forms.RadioSelect}

