# -*- coding:UTF-8 -*-
from django import forms
from courses.models import Course, Lesson


class CourseModelForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

class LessonModelForm(forms.ModelForm):

    class Meta:
        model = Lesson
        #exclude = ['course']
        labels = {'order': 'ID'}
        fields = '__all__'
