
from django.contrib import admin
from courses.models import Course, Lesson
from students.models import Student



# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Student)