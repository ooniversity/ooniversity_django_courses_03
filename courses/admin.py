from django.contrib import admin
from courses.models import Course
from courses.models import Lesson
from courses.models import Student

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Student)
