from courses.models import Course, Lesson
from django import forms

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course

class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
