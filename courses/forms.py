# -*- coding: utf-8 -*-

from django import forms
from students.models import Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

