# -*- coding: utf-8 -*-
from django import forms
from models import Course


class CourceModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
