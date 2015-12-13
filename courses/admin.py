from django.contrib import admin
from courses.models import Course, Lesson
from students.models import Student

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name','short_description']
    search_fields = ['name']

admin.site.register(Course, CoursesAdmin)
admin.site.register(Lesson)
