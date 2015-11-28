from django.contrib import admin
from courses.models import Course, Lesson
from students.models import Student

admin.site.register(Course)
admin.site.register(Lesson)
