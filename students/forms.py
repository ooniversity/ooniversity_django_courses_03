# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from courses.models import Course
from students.models import Student


class StudentModelForm(forms.ModelForm):
    class Meta:
    	model = Student
