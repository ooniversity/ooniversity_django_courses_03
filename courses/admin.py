from django.contrib import admin

from courses.models import Course, Lesson

class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'short_description', 'coach', 'assistant']
    list_display = ('name', 'short_description', 'description', 'coach', 'assistant')
    search_fields = ['name']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)


 

