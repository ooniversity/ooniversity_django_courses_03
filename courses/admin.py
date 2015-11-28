from django.contrib import admin
from courses.models import Course, Lesson


class CourseAdmin(admin.ModelAdmin):
    list_display = ('description','name')

admin.site.register(Course)
admin.site.register(Lesson)
