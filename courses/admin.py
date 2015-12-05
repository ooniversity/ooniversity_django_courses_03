from django.contrib import admin
from courses.models import Course, Lesson

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']
    search_fields = ['name']




admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)


