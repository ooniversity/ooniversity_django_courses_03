from django.forms import ModelForm
from courses.models import Course, Lesson


class CourseModelForm(ModelForm):
	class Meta:
		model = Course
		

class LessonModelForm(ModelForm):
	class Meta:
		model = Lesson

