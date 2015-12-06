from django import forms
import models


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'


class LessonModelForm(forms.ModelForm):
    class Meta:
        model = models.Lesson
        fields = '__all__'
